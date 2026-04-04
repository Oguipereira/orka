from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def billing_root():
    return {"module": "billing", "status": "ok"}
