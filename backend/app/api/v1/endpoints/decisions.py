from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def decisions_root():
    return {"module": "decisions", "status": "ok"}
