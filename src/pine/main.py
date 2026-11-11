from fastapi import FastAPI

from pine.api.routes import router

app = FastAPI(
    title="pine",
    description="a moodle and personal notes rag thing",
    version="0.1.0",
)

app.include_router(router)


@app.get("/health")
async def health():
    return {"status": "ok"}
