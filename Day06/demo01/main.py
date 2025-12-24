from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
import os

load_dotenv()
conversation=[]

llm= init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

agent=create_agent(model=llm, tools=[],system_prompt="You are helpful assistant. just answer in short but accurate")


while True:
    User_prompt=input("Ask:-")
    if User_prompt == "exit":
        break
    
    conversation.append({"role":"user","content": User_prompt})
    
    result=agent.invoke({"messages":conversation })

    ai_msg=result["messages"][-1]

    print("AI:-",ai_msg.content)

    conversation=result["messages"]