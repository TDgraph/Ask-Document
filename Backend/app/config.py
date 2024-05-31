# Import BaseSettings from pydantic_settings
from pydantic_settings import BaseSettings

# Define a Settings class that extends BaseSettings
class Settings(BaseSettings):
    # Database configuration variables
    DATABASE_HOSTNAME: str
    DATABASE_PORT: str
    DATABASE_PASSWORD: str
    DATABASE_USERNAME: str
    DATABASE_NAME: str

    #HuggingFace Configuration variables
    HUGGINGFACEHUB_API_TOKEN: str

    # Uncomment and configure these settings if you need them
    # LangChain Configuration
    # LANGCHAIN_TRACING_V2: bool = True
    # LANGCHAIN_ENDPOINT: str = "https://api.smith.langchain.com"
    # LANGCHAIN_API_KEY: str

    # OpenAI Configuration
    # OPENAI_API_KEY: str

    # Specify the configuration class for Pydantic
    class Config:
        # Load environment variables from a .env file
        env_file = ".env"

# Create an instance of the Settings class
settings = Settings()
