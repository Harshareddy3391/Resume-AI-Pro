from fastapi import HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.models.document_model import Document
from app.models.user_model import User 
from app.services.pdf_services import extract_text

from app.services.storage_service import (
    upload_pdf,
    delete_pdf
)


def create_document(
    db: Session,
    file: UploadFile,
    current_user: User
):
    """
    Upload PDF to Supabase Storage and save document metadata in PostgreSQL.
    """

    # Upload file to Supabase Storage
    uploaded_file = upload_pdf(
    file=file,
    user_id=current_user.id
)

    text = extract_text(uploaded_file["file_bytes"]) 
    print("=" * 50)
    print("EXTRACTED TEXT")
    print("=" * 50)
    print(text)
    print("=" * 50)

    # Create document object
    document = Document(
        filename=uploaded_file["filename"],
        file_path=uploaded_file["storage_path"],
        file_size=uploaded_file["file_size"],
        user_id=current_user.id
    )

    # Save to database
    db.add(document)
    db.commit()
    db.refresh(document)

    return document


def delete_document(
    db: Session,
    document_id: int,
    current_user: User
):
    """
    Delete document from Supabase Storage and remove metadata from PostgreSQL.
    """

    document = (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.user_id == current_user.id
        )
        .first()
    )

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found."
        )

    # Delete from Supabase Storage
    delete_pdf(document.file_path)

    # Delete from PostgreSQL
    db.delete(document)
    db.commit()

    return {
        "message": "Document deleted successfully."
    }