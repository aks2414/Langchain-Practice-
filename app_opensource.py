#import os
#from transformers import AutoTokenizer, AutoModelForCausalLM
#import streamlit as st

# Model name
#model_name = "EleutherAI/gpt-neox-20B"

# Load pre-trained model and tokenizer
#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForCausalLM.from_pretrained(model_name)

# Streamlit framework
#st.title("Langchain Demo with GPT-NeoX-20B")
input_text = st.text_input('Search anything')

# Use the model
if input_text:
    # Encode the input text
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # Generate a response
    output = model.generate(input_ids, max_length=100, temperature=0.8, do_sample=True)

    # Decode the response
    output_text = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    st.write(output_text)
