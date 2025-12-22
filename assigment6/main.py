import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page title
st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 AI Chatbot (Groq | LM Studio)")

# Sidebar
with st.sidebar:
    st.header("Model Selection")
    model_choice = st.selectbox("Choose Model", ["Groq", "LM Studio"])

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask something...")

# --------- API FUNCTIONS ---------

def call_groq(messages):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": messages
    }

    res = requests.post(url, headers=headers, json=payload)
    data = res.json()

    if "choices" not in data:
        raise Exception(data)

    return data["choices"][0]["message"]["content"]

def call_lmstudio(messages):
    url = "http://localhost:1234/v1/chat/completions"
    payload = {
        "model": "meta-llama-3-8b-instruct",
        "messages": messages,
        "temperature": 0.7
    }
    response = requests.post(url, json=payload)
    return response.json()["choices"][0]["message"]["content"]

# --------- CHAT FLOW ---------

if user_input:
    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                if model_choice == "Groq":
                    reply = call_groq(st.session_state.messages)
                else:
                    reply = call_lmstudio(st.session_state.messages)

                st.markdown(reply)

                # Store assistant message
                st.session_state.messages.append(
                    {"role": "assistant", "content": reply}
                )

            except Exception as e:
                st.error(f"Error: {e}")
