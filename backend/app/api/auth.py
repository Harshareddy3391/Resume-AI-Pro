from authlib.integrations.starlette_client import OAuth

from fastapi import APIRouter,Depends,Request

from sqlalchemy.orm import Session

from app.core.config import settings

from app.db.database import get_db





router=APIRouter(prefix="/auth",
                 tags=["Authentication"])

oauth=OAuth()

oauth.register(
    name="google",
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope":"openid email profile"
    }
)


@router.get("/google/login")
async def google_login(request:Request):
    """
    Redirect the user to google's login page
    """

    redirect_url=settings.GOOGLE_REDIRECT_URL



    return await oauth.google.authorize_redirect(
        request,
        redirect_url
    )