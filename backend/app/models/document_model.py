from sqlalchemy import Column,Integer,ForeignKey,String,DateTime

from sqlalchemy.sql import func

from sqlalchemy.orm import relationship 


from app.db.database import Base


class Document(Base):


    __tablename__ = "documents"

    id=Column(Integer,primary_key=True,index=True)
    filename=Column(String,nullable=False)
    file_path=Column(String,nullable=False)
    file_size=Column(Integer,nullable=False)


    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    uploaded_at=Column(DateTime(timezone=True),server_default=func.now())
    user=relationship("User",back_populates="documents")