import httpx
from datetime import datetime, timedelta, timezone
from app.core.config import settings
from app.core.security import encrypt_token


class MercadoLivreIntegration:
    platform = "mercado_livre"
    BASE = "https://api.mercadolibre.com"
    TOKEN_URL = "https://api.mercadolibre.com/oauth/token"

    def __init__(self, access_token: str = "", refresh_token: str = ""):
        self.access_token  = access_token
        self.refresh_token = refresh_token

    @staticmethod
    def get_auth_url(state: str = "orka") -> str:
        return (
            f"https://auth.mercadolivre.com.br/authorization"
            f"?response_type=code"
            f"&client_id={settings.ML_APP_ID}"
            f"&redirect_uri={settings.ML_REDIRECT_URI}"
            f"&state={state}"
        )

    @staticmethod
    async def exchange_code(code: str) -> dict:
        async with httpx.AsyncClient() as c:
            r = await c.post(MercadoLivreIntegration.TOKEN_URL, data={
                "grant_type":    "authorization_code",
                "client_id":     settings.ML_APP_ID,
                "client_secret": settings.ML_CLIENT_SECRET,
                "code":          code,
                "redirect_uri":  settings.ML_REDIRECT_URI,
            })
            r.raise_for_status()
            data = r.json()
            return {
                "access_token":  encrypt_token(data["access_token"]),
                "refresh_token": encrypt_token(data["refresh_token"]),
                "expires_at":    datetime.now(timezone.utc) + timedelta(seconds=data.get("expires_in", 21600)),
                "user_id":       data.get("user_id"),
            }

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.access_token}"}

    async def get_orders(self, seller_id: str, limit: int = 50) -> list[dict]:
        async with httpx.AsyncClient() as c:
            r = await c.get(f"{self.BASE}/orders/search", headers=self._headers(), params={
                "seller": seller_id, "sort": "date_desc", "limit": limit,
            })
            r.raise_for_status()
            return [{
                "external_id":  str(o["id"]),
                "date":         o.get("date_created"),
                "total_amount": o.get("total_amount", 0),
                "status":       o.get("status", ""),
                "channel":      "mercado_livre",
            } for o in r.json().get("results", [])]

    async def get_products(self, seller_id: str) -> list[dict]:
        async with httpx.AsyncClient(timeout=30) as c:
            r = await c.get(
                f"{self.BASE}/users/{seller_id}/items/search",
                headers=self._headers(), params={"limit": 50},
            )
            r.raise_for_status()
            ids = r.json().get("results", [])
            if not ids:
                return []
            r2 = await c.get(
                f"{self.BASE}/items",
                headers=self._headers(), params={"ids": ",".join(ids[:20])},
            )
            r2.raise_for_status()
            return [{
                "external_id": i.get("body", {}).get("id", ""),
                "name":        i.get("body", {}).get("title", ""),
                "sku":         i.get("body", {}).get("seller_sku", ""),
                "price":       i.get("body", {}).get("price", 0),
            } for i in r2.json() if i.get("code") == 200]

    async def get_inventory(self, **kwargs) -> list[dict]:
        return []

    async def get_financials(self, **kwargs) -> dict:
        return {}
