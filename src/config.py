import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

def _req(name: str) -> str:
    val = os.getenv(name)
    if not val:
        raise RuntimeError(f"Missing required env var: {name}")
    return val

@dataclass(frozen=True)
class Settings:
    # Azure AI Search
    AZURE_AI_SEARCH_SERVICE_NAME: str
    AZURE_AI_SEARCH_INDEX_NAME: str
    AZURE_AI_SEARCH_API_KEY: str

    # Azure OpenAI
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_API_VERSION: str
    AZURE_OPENAI_MODEL: str

def get_settings() -> Settings:
    return Settings(
        AZURE_AI_SEARCH_SERVICE_NAME=_req("AZURE_AI_SEARCH_SERVICE_NAME"),
        AZURE_AI_SEARCH_INDEX_NAME=_req("AZURE_AI_SEARCH_INDEX_NAME"),
        AZURE_AI_SEARCH_API_KEY=_req("AZURE_AI_SEARCH_API_KEY"),
        AZURE_OPENAI_ENDPOINT=_req("AZURE_OPENAI_ENDPOINT"),
        AZURE_OPENAI_API_KEY=_req("AZURE_OPENAI_API_KEY"),
        AZURE_OPENAI_API_VERSION=_req("AZURE_OPENAI_API_VERSION"),
        AZURE_OPENAI_MODEL=_req("AZURE_OPENAI_MODEL"),
    )
