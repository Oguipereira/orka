from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_ENV: str = "development"
    SECRET_KEY: str = "change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DATABASE_URL: str = "postgresql+asyncpg://orka:orka@localhost:5432/orka_db"
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/1"

    FRONTEND_URL: str = "http://localhost:3000"

    ML_APP_ID: str = ""
    ML_CLIENT_SECRET: str = ""
    ML_REDIRECT_URI: str = "http://localhost:8002/api/v1/integrations/mercadolivre/callback"

    SHOPIFY_CLIENT_ID: str = ""
    SHOPIFY_CLIENT_SECRET: str = ""
    SHOPIFY_REDIRECT_URI: str = ""
    SHOPIFY_API_KEY: str = ""
    SHOPIFY_API_SECRET: str = ""

    STRIPE_CLIENT_ID: str = ""
    STRIPE_SECRET_KEY: str = ""

    MP_CLIENT_ID: str = ""
    MP_CLIENT_SECRET: str = ""
    MP_REDIRECT_URI: str = ""

    AMAZON_LWA_CLIENT_ID: str = ""
    AMAZON_CLIENT_ID: str = ""
    AMAZON_CLIENT_SECRET: str = ""

    NUVEMSHOP_CLIENT_ID: str = ""
    NUVEMSHOP_CLIENT_SECRET: str = ""

    BLING_CLIENT_ID: str = ""
    BLING_CLIENT_SECRET: str = ""
    BLING_REDIRECT_URI: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
