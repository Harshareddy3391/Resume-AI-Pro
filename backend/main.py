from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from app.core.config import settings
from app.api.auth import router as auth_router
from app.api.user import router as user_router
app=FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG

)


#session middleware (required for google auth)
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.JWT_SECRET_KEY
)

#include router
app.include_router(auth_router)
app.include_router(user_router)
@app.get("/")
def root():
    return {
        "message":"welcome to DocuChat AI",
        "debug":settings.APP_VERSION
    }




@app.get("/health")
def health_check():
    return {
        "status":"healthy",
        "application":settings.APP_NAME
    }