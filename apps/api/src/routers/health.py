from fastapi import APIRouter

router = APIRouter(prefix="", tags=["health"])


@router.get("/")
async def get_health():
    # TODO: add more sophisticated checks
    return "healthy"
