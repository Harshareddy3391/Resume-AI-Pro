from sqlalchemy import Column,Integer,String,DateTime
from app.db.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class User(Base):

    __tablename__="users"


    id=Column(Integer,primary_key=True,index=True)
    google_id=Column(String(255),nullable=True,unique=True)
    name=Column(String(100),nullable=False)
    email=Column(String(100),unique=True,nullable=False)
    picture=Column(String(500),nullable=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

    updated_at=Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    

    documents=relationship(
        "Document",
        back_populates="user",
        cascade="all, delete-orphan"
    )