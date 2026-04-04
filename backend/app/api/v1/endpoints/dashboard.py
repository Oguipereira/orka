from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def dashboard_root():
    return {"module": "dashboard", "status": "ok"}
