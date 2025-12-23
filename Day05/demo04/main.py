import os
import certifi
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

# 🔐 Fix SSL issue on Windows
os.environ["SSL_CERT_FILE"] = certifi.where()

load_dotenv()

llm = init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

conversation = [
    {"role": "system", "content": "You are a helpful assistant"}
]

k = int(input("enter k value="))

while True:
    user_input = input("You:-")
    if user_input.lower() == "exit":
        break

    conversation.append({"role": "user", "content": user_input})

    # Keep system + last k user/assistant pairs
    system_msg = conversation[0]
    recent_msgs = conversation[-k * 2:]
    context = [system_msg] + recent_msgs

    llm_output = llm.invoke(context)  # ✅ FIXED
    print("AI:-", llm_output.content)

    conversation.append({"role": "assistant", "content": llm_output.content})
