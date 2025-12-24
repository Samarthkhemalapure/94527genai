from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()

@tool
def calculator(expression):
    """
    this caluculator function solves any arithmatic expression contaning all constant values.
    it supports basic operators +,-,*,/ and paranthesis
    :parameter expression: str input arithmetic expression
    :returns expression result as str
    """
    try:
        result=eval(expression)
        return(result)
    except:
        return"error: cannot solve expression"

@tool
def get_wheather(city):
    """ 
    this get_weather function gets the current weather of given city.
    if weather cannot be found, it returns 'error.
    this function dosen't return historic  or genera weather of city,
    :parameter city: str input-city name
    :returns current weather in json format or  'error'
    """    
    try:
        api_key=os.getenv("OPENWEATHER_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
        resonse=requests.get(url)
        weather=resonse.json()
        return json.dumps(weather)
    except:
        return "ERROR!!!!"

@tool
def read_file(filepath):
    """
    Reads the contents of a text file from the given file path.
    """
    with open(filepath,'r') as file:
        text=file.read()
        return text
    
llm=init_chat_model(
    model="meta-llama-3.1-8b-instruct",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="dummyeky"
)

#create agent
agent=create_agent(model=llm,tools=[calculator,get_wheather,read_file],system_prompt="you are helful assistant.answer in short ")

while True:
    user_input=input("Ask:-")
    if user_input == "exit":
        break

    result=agent.invoke({
        "messages":[{"role": "user","content": user_input}]
        })
    
    llm_output=result["messages"][-1]
    print("AI:-",llm_output.content)
    #print("\n \n",result["messages"])