## Integrate our code OpenAI API

import os
from langchain.llms import OpenAI 
from langchain import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv



os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

import streamlit as st

# streamlit framework

st.title("Celebrity Search using OpenAI API")
input_text = st.text_input('Search anything')

# Prompt Templates

first_input_prompt = PromptTemplate(
    input_variables = ['name'],
    template = "Tell me abbout {name}.",
)

# OpenAI LLM Model

llm = OpenAI(temperature = 0.8)

# OpenAI LLM Chain
chain1 = LLMChain(llm = llm, prompt = first_input_prompt, verbose = True)

if input_text:
    st.write(chain1.run(input_text))
    
    
