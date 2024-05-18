## PDF Query using Langchain LLM

from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

pdfreader = PdfReader('Internship Letter - Aditya Kumar Singh.pdf')

from typing_extensions import Concatenate
# read text from pdf
raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content
        

