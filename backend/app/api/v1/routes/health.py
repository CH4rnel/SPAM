# ♃ ☿ 𓂀  SPAM CONFIG LAYER 𓂀  ☿ ♃

from fastapi import APIRouter

router = APIRouter(
    tags=["system"],
)


@router.get("/health")
async def health_check() -> dict[str, str]:
    """
    Basic backend health check endpoint.
    """

    return {
        "status": "ok",
        "service": "SPAM backend",
    }
