from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")


@router.get("/")
async def root():
    return {"message": "hello world!!, ci test"}
