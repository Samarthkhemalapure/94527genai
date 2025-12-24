from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool

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
    

#create model
llm=init_chat_model(
    model="meta-llama-3.1-8b-instruct",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="dummykey"
)

#create agent
agent=create_agent(model=llm, tools=[calculator],system_prompt="You are helpful assistant.answer in short but accurate")

while True:
    #take user input
    User_prompt=input("Ask:-")
    if User_prompt == "exit":
        break

    result=agent.invoke({
        "messages":[
            {"role":"user","content":User_prompt }
             ]})

    llm_output=result["messages"][-1]
    print("Ai:-",llm_output.content)
    print("\n \n",result["messages"])