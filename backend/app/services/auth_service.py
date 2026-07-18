from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.auth_schema import GoogleUser
from app.utils.jwt import create_access_tocken

def get_or_create_user(db: Session, google_user: GoogleUser) -> str:
    """
    Get an existing user or create a new user,
    then return a JWT access token.
    """

    # Check whether the user exists
    user = (
        db.query(User)
        .filter(User.email == google_user.email)
        .first()
    )

    # Create a new user if not found
    if user is None:
        user = User(
            google_id=google_user.google_id,
            name=google_user.name,
            email=google_user.email,
            picture=google_user.picture,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

    # Generate JWT for both existing and new users
    access_tocken = create_access_tocken(
        {
            "sub": user.email,
            "user_id": user.id,
        }
    )

    return access_tocken