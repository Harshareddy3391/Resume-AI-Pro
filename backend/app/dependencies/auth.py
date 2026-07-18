from fastapi import Depends,HTTPException,status


from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session



from app.db.database import get_db
from app.models.user_model import User
from app.utils.jwt import verify_access_tocken



oauth2_schema=OAuth2PasswordBearer(
    tokenUrl="auth/google/login"
)

def get_current_user(
    tocken:str=Depends(oauth2_schema),db:Session=Depends(get_db)
):
    payload=verify_access_tocken(tocken)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    user_id=payload.get("user_id")
    

    if user_id is None:
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    
    user=db.quary(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return user