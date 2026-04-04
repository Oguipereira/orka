from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.base import get_db
from app.models.integration import Integration

router = APIRouter()

@router.get("/")
async def list_integrations(org_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Integration).where(Integration.organization_id == org_id))
    integrations = result.scalars().all()
    return [{"id": str(i.id), "platform": i.platform, "expires_at": i.expires_at} for i in integrations]

@router.get("/mercadolivre/connect")
async def connect_mercadolivre():
    from app.core.config import settings
    url = (
        f"https://auth.mercadolivre.com.br/authorization"
        f"?response_type=code&client_id={settings.ML_APP_ID}"
        f"&redirect_uri={settings.ML_REDIRECT_URI}"
    )
    return {"redirect_url": url}

@router.get("/mercadolivre/callback")
async def mercadolivre_callback(code: str, db: AsyncSession = Depends(get_db)):
    # TODO: trocar code por tokens via httpx
    return {"message": "callback recebido", "code": code}
