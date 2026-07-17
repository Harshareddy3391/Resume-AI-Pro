from datetime import datetime,timedelta,timezone

from jose import jwt
from app.core.config import settings


def create_access_tocken(data:dict):
    "create a jwt acces tocken"

    # Create a copy of the payload
    to_encode=data.copy()



    #set the tocken expire time
    expire=datetime.now(timezone.utc)+timedelta(minutes=settings.ACCESS_TOCKEN_EXPIRE_MINUTES)


    #add expiration time to payload
    to_encode.update({"exp":expire})


    #Encode the Jwt
    tocken=jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY
    )

    return tocken