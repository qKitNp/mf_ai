from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv
import os
import streamlit as st


GOOGLE_API_KEY = st.secrets["API_KEY"]
COHERE_API_KEY = st.secrets["COHERE_KEY"]

def get_embeddings():
    os.write(1, f"Getting embeddings\n".encode())
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    return embeddings

def get_cohere_embeddings():
    os.write(1, f"Getting cohere embeddings\n".encode())
    embeddings = CohereEmbeddings(model="embed-english-v3.0",cohere_api_key=COHERE_API_KEY)
    return embeddings

if __name__ == '__main__':
    print(get_cohere_embeddings())