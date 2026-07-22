from fastapi import HTTPException,UploadFile,status

from sqlalchemy.orm import Session 

from app.models.document_model import Document
from app.models.user_model import User


from app.services.service_storage import (UploadFile,delete_pdf)




def create_document(
        db:Session,file:UploadFile,current_user:User

):
    
    """
    Upload PDF to supabase storage and save documet metadata in postgreSQL.
    """

    #Upload file to supabase storage
    uploaded_file=UploadFile(file=file,user_id=current_user.id)


    #create document obj
    document=Document(
        filename=uploaded_file["filename"],
        storage_path=uploaded_file["storage_path"],
        file_size=uploaded_file["file_size"],
        user_id=current_user.id
    )



    #save to database
    db.add(document)
    db.commit()
    db.refresh(document)


    return document

def get_user_document(
        db:Session,
        current_user:User
):
    
    """
    Return all documents uploaded by the current user.
    """

    documents=(
        db.query(Document)
        .filter(Document.user_id == current_user.id)
        .order_by(Document.uploaded_at.desc).all()
    )


    return documents

def delete_document(
        db:Session,
        document_id:int,
        current_user:User
):
    
    """
    Delete document from supabase storage and remove metadata from postgresql.
    """

    document=(
        db.query(Document).filter(Document.id == document.id,Document.user_id == current_user.id).first()
    )

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document Not Founded."
        )
    #Delete from supabase storage
    delete_pdf(document.storage_path)


    #Delete from PostgreSql
    db.delete(document)
    db.commit()


    return  {
        "message":"Document deleted successfully"
    }