from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from .config import Settings
from .retriever import build_retriever
from .llm import build_llm
from .prompts import get_rag_prompt

def build_chain(settings: Settings):
    retriever = build_retriever(settings)
    llm = build_llm(settings)
    prompt = get_rag_prompt()

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain
