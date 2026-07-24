from datetime import datetime, timezone, timedelta
from typing import Any
from jose import jwt, JWTError

from app.core.config import settings


def create_access_tocken(data: dict[str, Any]) -> str:
    """
    Create a JWT access tocken
    """

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOCKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    access_tocken = jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return access_tocken


def verify_access_tocken(tocken: str) -> dict[str, Any] | None:
    """
    Verify and decode jwt tocken
    """
    try:
        payload = jwt.decode(
            tocken,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )

        return payload

    except JWTError:
        return None