from pydantic_settings import BaseSettings
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


class Settings(BaseSettings):
    DB_USERNAME:str = "ayanpostgres"
    DB_HOST:str = "vehicle-staging-db.postgres.database.azure.com"
    DB_PORT:str = "5432"
    DB_NAME:str = "vehicle_db"
    KEY_VAULT_NAME:str
    SECRET_NAME: str

    class Config:
        env_file=".env"
        case_sensitive=True

    @property
    def database_password(self) -> str:
        vault_url=f"https://{self.KEY_VAULT_NAME}.vault.azure.net/"
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=vault_url,credential=credential)
        secret = client.get_secret(self.SECRET_NAME)
        return secret.value

    @property
    def DATABASE_URL(self) -> str:
        return(
            f"postgresql://{self.DB_NAME}:{self.database_password}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?sslmode=require"
        )

settings=Settings()
