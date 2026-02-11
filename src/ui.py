import streamlit as st

def init_page():
    st.set_page_config(page_title="ResearchAI Chatbot", page_icon="📚")
    st.title("📚 ResearchAI Chatbot")
    st.caption("Powered by Azure AI Search + Azure OpenAI")

def init_chat_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def render_history():
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

def chat_input_box() -> str | None:
    return st.chat_input("How can I assist you with your research today?")

def append_message(role: str, content: str):
    st.session_state.messages.append({"role": role, "content": content})
