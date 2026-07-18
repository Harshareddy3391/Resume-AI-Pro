from authlib.integrations.starlette_client import OAuth

from fastapi import APIRouter,Depends,Request

from sqlalchemy.orm import Session

from app.core.config import settings

from app.db.database import get_db

from app.schemas.auth_schema import GoogleUser

from app.services.auth_service import get_or_create_user








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

    redirect_url=settings.GOOGLE_REDIRECT_URI



    return await oauth.google.authorize_redirect(
        request,
        redirect_url
    )



@router.get("/google/callback")
async def google_callback(request:Request,db:Session=Depends(get_db)):

    """
    Google oAuth callback
    """

    #Exchange authorization code for access tocken
    tocken=await oauth.google.authorize_access_token(
        request

    )


    #get google information
    user_info=tocken["userinfo"]

    google_user=GoogleUser(
        google_id=user_info["sub"],
        name=user_info["name"],
        email=user_info["email"],
        picture=user_info["picture"]

    )

    access_tocken=get_or_create_user(db,google_user)


    return {
        "access_tocken":access_tocken,
        "tocken_type":"bearer"
    }
