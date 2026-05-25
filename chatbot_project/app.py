import streamlit as st
from chatbot_ai import get_response

st.set_page_config(page_title="Advanced AI Chatbot", page_icon="🤖")

st.title("🤖 Advanced AI Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask anything:")

if user_input:
    bot_reply = get_response(user_input)

    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", bot_reply))

for sender, msg in st.session_state.chat:
    if sender == "You":
        st.write("🧑", msg)
    else:
        st.write("🤖", msg)