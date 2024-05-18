## Integrate our code OpenAI API

import os
from langchain.llms import OpenAI 
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

import streamlit as st

# streamlit framework

st.title("Langchain Demo with OPENAI API")
input_text = st.text_input('Search anything')

# OpenAI LLM Model

llm = OpenAI(temperature = 0.8)

if input_text:
    st.write(llm(input_text))
    
    
