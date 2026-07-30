# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def root():

    return {
        "project": "SPAM Network",
        "status": "online"
    }



@router.get("/health")
async def health():

    return {
        "status": "healthy"
    }
