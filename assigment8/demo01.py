from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
import requests
import os

load_dotenv()
api = os.getenv("open_weather")

@tool
def calculator(expression: str) -> str:
    """Evaluate a math expression."""
    try:
        return str(eval(expression))
    except:
        return "Error: invalid expression"


@tool
def read_file(filepath: str) -> str:
    """Return file contents exactly from provided path."""
    if not os.path.exists(filepath):
        return f"Error: {filepath} does not exist"
    try:
        with open(filepath, "r") as f:
            return f.read()
    except:
        return "Error reading file"


@tool
def current_weather(city: str) -> str:
    """Get current weather from Openweather """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={user}&appid={api}&units=metric"
        response = requests.get(url)
        data = response.json()
        temp=data['main']['temp']
        desc=data['weather'][0]['description']
        return f"Weather in {city}: {temp}°C, {desc}"
    except Exception as e:
        return f"Weather error: {e}"


@tool
def knowledge_lookup(query: str) -> str:
    """Lookup quick facts from DuckDuckGo."""
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        data = requests.get(url, timeout=5).json()
        return data.get("Abstract", "No clear answer found.")
    except Exception as e:
        return f"Lookup error: {e}"


llm = init_chat_model(
    model="meta-llama-3.1-8b-instruct",     
    model_provider="openai",                
    base_url="http://127.0.0.1:1234/v1",   
    api_key="dummy"                        
)


agent = create_agent(
    model=llm,
    tools=[calculator, read_file, current_weather, knowledge_lookup],
    system_prompt="""
You are a strict tool-using assistant.

RULES:
1. If input is a math expression -> USE calculator.
2. If message contains *.txt, *.csv, *.json -> USE read_file with same filename.
3. If user asks weather -> USE current_weather.
4. If user asks who/what/when/where/why -> USE knowledge_lookup.
5. DO NOT answer by yourself when a tool is applicable.
6. DO NOT explain tool usage. Just provide the final answer from the tool.
""",
)

print("\n🚀 Tool Agent Ready (type 'exit' to quit)\n")

while True:
   user = input("Ask Anything : ")

   if user.lower() == "exit":
    break
   
   result = agent.invoke(
       {
           "messages":[
               {
                   "role":"user",
                   "content":user
               }
           ]
       }
    )
   
   output = result["messages"][-1]
   print("\nAI:\n")
   print(output.content)
   print("-" * 50)