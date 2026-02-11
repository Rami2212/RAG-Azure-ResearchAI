from langchain_openai import AzureChatOpenAI
from .config import Settings

def build_llm(settings: Settings) -> AzureChatOpenAI:
    return AzureChatOpenAI(
        api_version=settings.AZURE_OPENAI_API_VERSION,
        azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
        api_key=settings.AZURE_OPENAI_API_KEY,
        deployment_name=settings.AZURE_OPENAI_MODEL,
    )
