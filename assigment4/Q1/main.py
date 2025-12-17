import streamlit as st
import time

st.title("Simple Streaming Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

def stream_reply(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.25)

if user_input:
    # Save and display user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Bot reply (echo)
    bot_reply = f"You said: {user_input}"

    # Save bot message
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    # Stream bot reply
    with st.chat_message("assistant"):
        st.write_stream(stream_reply(bot_reply))