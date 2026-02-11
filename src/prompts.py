from langchain_core.prompts import ChatPromptTemplate

def get_rag_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages([
        ("system", "Answer the question using only the provided context."),
        ("human", "Context:\n{context}\n\nQuestion:\n{question}")
    ])
