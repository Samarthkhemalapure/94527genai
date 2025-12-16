import streamlit as st 

#Input Widgets
name=st.text_input("Enter your name:-")

message=st.text_input("Enter your Message:-")

upload_file=st.file_uploader("Choose a file",type=['txt','pdf','csv'])

model=st.selectbox("Choose AI Model:-",["GPT-4","Llama 3","Gemini","Claude"])

#dispaly Widges
if name:
    st.write(f"Hello ,{name}")


st.markdown("** This is bold text** and **this is italic**")

#display dataframe
import pandas as pd 
df=pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})

st.dataframe(df)

#display json
config={"model": "gpt-4","temperature": 0.7,"max_tokens": 500}
st.json(config)