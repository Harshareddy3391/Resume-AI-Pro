from fastapi import FastAPI
from app.core.config import settings

app=FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION

)

@app.get("/")
def root_a():
    return {
        "message":"welcome to DocuChat AI",
        "debug":settings.DEBUG
    }