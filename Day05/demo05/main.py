from langchain.chat_models  import init_chat_model
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

llm=init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

conversation=[{"role":"system","content": "you are sql expert develope with 10-15 years of experience"}]

csv_file=input("Enter path of csv file:0-")
df=pd.read_csv(csv_file)
print("CSV Schema:-")
print(df.dtypes)

while True:
    user_input=input("Ask anything about this csv=")
    if user_input =="exit":
        break
    llm_input=f"""
            table name:data
            table schema:{df.dtypes}
            question:{user_input}
            instruction:
            Write a SQL query for the above question. 
            Generate SQL query only in plain text format and nothing else.
            If you cannot generate the query, then output 'Error'."""
    result=llm.invoke(llm_input)
    print(result.content)