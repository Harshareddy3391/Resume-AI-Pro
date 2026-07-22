from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # ==========================
    # Application
    # ==========================
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool


    # ==========================
    # Database
    # ==========================
    DATABASE_URL: str

    # ==========================
    # Google OAuth
    # ==========================
    GOOGLE_CLIENT_ID:str
    GOOGLE_CLIENT_SECRET:str
    GOOGLE_REDIRECT_URI:str

       # ==========================
    # JWT
    # ==========================
    JWT_SECRET_KEY:str
    JWT_ALGORITHM:str
    ACCESS_TOCKEN_EXPIRE_MINUTES:int

    # ==========================
    # Supabase Storage
    # ==========================
    SUPABASE_URL:str
    SUPABASE_KEY:str
    SUPABASE_BUCKET:str




    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()