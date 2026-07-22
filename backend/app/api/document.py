"""
Document API Router
 This file handles al document-related HTTP endpoints.

 Responsibilities:
 1.Upload PDF 
 2.Get all Uploaded PDF'S
 3.Delete PDF

 The Router does NOT contain business logic.

 It simply calls the corresponding service function.
"""



from typing import List
from fastapi import APIRouter,Depends,UploadFile,status


from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user

from app.models.user_model import User

from app.schemas.document_schema import DocumentResponse
from app.services.document_service import (
    create_document,
    delete_document,
    get_user_document

)

#create router
router=APIRouter(prefix="/documents",
                 tags=['Documets'])


@router.post("/upload",
             response_model=DocumentResponse,
             status_code=status.HTTP_201_CREATED
             )
def upload_document(file:UploadFile=File(...),
                    db:Session=Depends(get_db),
                    current_user:User=Depends(get_current_user)
                    ):
    

    """
    Upload a PDF document.

    Flow:
    Client
      |
      API
      |
    document_services.created_document()
      |
    supabase storage 
      |
    postgreshSQL

    """

    return create_document(
        db=db,
        file=file,
        current_user=current_user
    )

@router.get( "/",responce_model=List[DocumentResponse]
            )
 
def get_documents(db:Session=Depends(get_db),
            current_user:User=Depends(get_current_user)):
    
    """
    Return all documents uploaded by the logged-in user
    """

    return get_current_user(
        db=db,
        current_user=current_user
    )

@router.delete(
    "/{document_id}"
)

def delete_document(
    document_id:int,
    db:Session=Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Delete a document .

    This deletes:
    1.PDF from supabase storage
    2.metadata from postgresql
    """

    return delete_document(
        db=db,
        document_id=document_id,
        current_user=current_user
    )