from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Settings for the application.
    """
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION : str
    APP_AUTHOR : str
    APP_AUTHOR_EMAIL : str

    ALLOWED_EXTENSIONS : list
    MAX_FILE_SIZE : int



    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    """
    Get the settings for the application.
    """
    return Settings()
        

