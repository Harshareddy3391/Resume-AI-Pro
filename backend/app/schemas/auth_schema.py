from pydantic import BaseModel,EmailStr



class GoogleUser(BaseModel):
    google_id:str
    name:str
    email:EmailStr
    picture:str | None=None


class TockenResponce(BaseModel):
    access_tocken:str
    tocken_type=str