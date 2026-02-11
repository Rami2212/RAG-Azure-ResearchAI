from langchain_community.retrievers import AzureAISearchRetriever
from .config import Settings

def build_retriever(settings: Settings) -> AzureAISearchRetriever:
    return AzureAISearchRetriever(
        service_name=settings.AZURE_AI_SEARCH_SERVICE_NAME,
        index_name=settings.AZURE_AI_SEARCH_INDEX_NAME,
        api_key=settings.AZURE_AI_SEARCH_API_KEY,
        content_key="answer",
        top_k=3,
    )
