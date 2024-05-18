## Integrate our code OpenAI API

import os
from langchain.llms import OpenAI 
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv



os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

import streamlit as st

# streamlit framework
st.title("Langchain Demo with OPENAI API")
input_text = st.text_input('What type of food do you want?')

# OpenAI LLM Model
llm = OpenAI(temperature = 0.8)

# Memory: Storing the conversation and making sure that you have the coversation saved in the database
title_memory = ConversationBufferMemory(input_key='type', memory_key='chat_history_type')
menu_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history_title')
price_memory = ConversationBufferMemory(input_key='menu', memory_key='chat_history_menu')


# Prompt Template 1
first_input_prompt = PromptTemplate(
    input_variables = ['type'],
    template = "Suggest me a restaurant name for {type} food."
)
# OpenAI LLM Chain1
chain1 = LLMChain(llm = llm, prompt = first_input_prompt, output_key = 'title', verbose = True, memory = title_memory)

# Prompt Template 2
second_input_prompt = PromptTemplate(
    input_variables = ['title'],
    template = "Build a menu for the {title}."
)
chain2 = LLMChain(llm=llm, prompt = second_input_prompt, verbose=True, output_key='menu', memory = menu_memory)

# Prompt Template 3
third_input_prompt = PromptTemplate(
    input_variables=['menu'],
    template = "What is the price of {menu}?"
)
chain3= LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='price', memory = price_memory)

# Simple Sequential Chain (Only shows the final output)
parent_chain_1 = SimpleSequentialChain(chains = [chain1, chain2, chain3], verbose =True)
parent_chain_2 = SequentialChain(chains = [chain1, chain2, chain3], verbose = True,
                                 input_variables = ['type'],
                                 output_variables = ['title', 'menu', 'price'])




#if input_text:
    # Using SimpleSequentialChain
    # st.write(parent_chain_1.run(input_text))
    
    # Using SequentialChain
    # st.write(parent_chain_2({'type':input_text}))
    
    

if input_text:
    st.write(parent_chain_2({'type':input_text}))

    with st.expander('Menu'): 
        st.info(menu_memory.buffer)

    with st.expander('Price'): 
        st.info(price_memory.buffer)