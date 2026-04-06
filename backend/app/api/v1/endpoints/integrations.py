from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from app.db.base import get_db
from app.core.deps import get_current_user, get_current_org_id
from app.core.config import settings
from app.models.user import User
from app.models.integration import Integration, IntegrationSyncLog
from app.services import integration as integration_service
import uuid

router = APIRouter()


@router.get("/")
async def list_integrations(
    current_user: User = Depends(get_current_user),
    org_id: str = Depends(get_current_org_id),
    db: AsyncSession = Depends(get_db),
):
    oid = uuid.UUID(org_id)
    result = await db.execute(
        select(Integration).where(Integration.organization_id == oid)
    )
    integrations = result.scalars().all()
    return [
        {
            "id": str(i.id),
            "platform": i.platform,
            "expires_at": i.expires_at.isoformat() if i.expires_at else None,
            "created_at": i.created_at.isoformat() if i.created_at else None,
        }
        for i in integrations
    ]


@router.get("/{integration_id}/logs")
async def get_sync_logs(
    integration_id: str,
    limit: int = Query(default=20, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(IntegrationSyncLog)
        .where(IntegrationSyncLog.integration_id == uuid.UUID(integration_id))
        .order_by(IntegrationSyncLog.last_sync_at.desc())
        .limit(limit)
    )
    logs = result.scalars().all()
    return [
        {
            "id": str(l.id),
            "status": l.status,
            "message": l.message,
            "last_sync_at": l.last_sync_at.isoformat() if l.last_sync_at else None,
        }
        for l in logs
    ]


# ── Generic connect URL ──────────────────────────────────────

@router.get("/connect/{platform}")
async def connect_url(
    platform: str,
    shop: str | None = None,
    current_user: User = Depends(get_current_user),
    org_id: str = Depends(get_current_org_id),
):
    urls: dict[str, str] = {
        "mercado_livre": (
            f"https://auth.mercadolivre.com.br/authorization"
            f"?response_type=code&client_id={settings.ML_APP_ID}"
            f"&redirect_uri={settings.ML_REDIRECT_URI}&state={org_id}"
        ) if settings.ML_APP_ID else "",
        "shopify": (
            f"https://{shop}/admin/oauth/authorize"
            f"?client_id={getattr(settings, 'SHOPIFY_CLIENT_ID', '')}"
            f"&scope=read_orders,read_products"
            f"&redirect_uri={getattr(settings, 'SHOPIFY_REDIRECT_URI', '')}"
            f"&response_type=code"
        ) if shop else "",
        "stripe": (
            f"https://connect.stripe.com/oauth/authorize"
            f"?response_type=code&client_id={getattr(settings, 'STRIPE_CLIENT_ID', '')}&scope=read_write"
        ),
        "mercadopago": (
            f"https://auth.mercadopago.com.br/authorization"
            f"?client_id={getattr(settings, 'MP_CLIENT_ID', '')}"
            f"&response_type=code&platform_id=mp"
            f"&redirect_uri={getattr(settings, 'MP_REDIRECT_URI', '')}"
        ),
        "amazon": (
            f"https://sellercentral.amazon.com.br/apps/authorize/consent"
            f"?application_id={getattr(settings, 'AMAZON_LWA_CLIENT_ID', '')}&state={org_id}&version=beta"
        ),
        "nuvemshop": (
            f"https://www.tiendanube.com/apps/{getattr(settings, 'NUVEMSHOP_CLIENT_ID', '')}/authorize"
        ),
        "bling": (
            f"https://bling.com.br/Api/v3/oauth/authorize"
            f"?response_type=code&client_id={getattr(settings, 'BLING_CLIENT_ID', '')}"
            f"&state={org_id}&redirect_uri={getattr(settings, 'BLING_REDIRECT_URI', '')}"
        ),
    }
    if platform not in urls:
        raise HTTPException(404, f"Plataforma '{platform}' não suportada")
    url = urls[platform]
    if not url:
        raise HTTPException(400, f"Credenciais para '{platform}' não configuradas no .env")
    return {"platform": platform, "redirect_url": url}


@router.delete("/{integration_id}")
async def disconnect_integration(
    integration_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Integration).where(Integration.id == uuid.UUID(integration_id))
    )
    integ = result.scalar_one_or_none()
    if not integ:
        raise HTTPException(404, "Integração não encontrada")
    await db.delete(integ)
    await db.commit()
    return {"status": "disconnected", "platform": integ.platform}


# ── Mercado Livre ────────────────────────────────────────────

@router.get("/mercadolivre/connect")
async def connect_mercadolivre(
    current_user: User = Depends(get_current_user),
):
    if not settings.ML_APP_ID:
        raise HTTPException(status_code=400, detail="ML_APP_ID não configurado no .env")
    url = (
        f"https://auth.mercadolivre.com.br/authorization"
        f"?response_type=code&client_id={settings.ML_APP_ID}"
        f"&redirect_uri={settings.ML_REDIRECT_URI}"
    )
    return {"redirect_url": url}


@router.get("/mercadolivre/callback")
async def mercadolivre_callback(
    code: str,
    org_id: str = Depends(get_current_org_id),
    db: AsyncSession = Depends(get_db),
):
    return await integration_service.ml_exchange_code(code, org_id, db)


@router.post("/mercadolivre/{integration_id}/sync")
async def sync_mercadolivre(
    integration_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await integration_service.sync_mercadolivre(integration_id, db)


# ── Shopify ──────────────────────────────────────────────────

@router.post("/shopify/{integration_id}/sync")
async def sync_shopify(
    integration_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await integration_service.sync_shopify(integration_id, db)


# ── Sync global ─────────────────────────────────────────────

@router.post("/sync-all")
async def sync_all(
    current_user: User = Depends(get_current_user),
    org_id: str = Depends(get_current_org_id),
    db: AsyncSession = Depends(get_db),
):
    oid = uuid.UUID(org_id)
    result = await db.execute(select(Integration).where(Integration.organization_id == oid))
    integrations = result.scalars().all()

    results = []
    for i in integrations:
        if i.platform == "mercado_livre":
            r = await integration_service.sync_mercadolivre(str(i.id), db)
        elif i.platform == "shopify":
            r = await integration_service.sync_shopify(str(i.id), db)
        else:
            r = {"status": "skipped"}
        results.append({"platform": i.platform, "result": r})

    return {"synced": len(results), "results": results}
