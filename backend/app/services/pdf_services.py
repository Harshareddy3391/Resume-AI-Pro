import fitz
from fastapi import HTTPException, status


def extract_text(file_bytes: bytes) -> str:
    try:
        pdf_document = fitz.open(stream=file_bytes, filetype="pdf")

        extracted_text = ""

        for page in pdf_document:
            extracted_text += page.get_text()

        pdf_document.close()

        return extracted_text.strip()

    except Exception as e:
        print("PDF ERROR:", e)   # <-- Add this line
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)        # <-- Change this line
        )