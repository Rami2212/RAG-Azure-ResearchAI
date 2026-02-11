import streamlit as st

from src.config import get_settings
from src.chain import build_chain
from src.ui import (
    init_page,
    init_chat_state,
    render_history,
    chat_input_box,
    append_message,
)

def main():
    init_page()
    init_chat_state()
    render_history()

    settings = get_settings()
    chain = build_chain(settings)

    user_query = chat_input_box()
    if not user_query:
        return

    append_message("user", user_query)
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chain.invoke(user_query)
            st.write(response)

    append_message("assistant", response)

if __name__ == "__main__":
    main()
