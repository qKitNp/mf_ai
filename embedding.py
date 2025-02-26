from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

GOOGLE_API_KEY = st.secrets["API_KEY"]

def get_embeddings():
    os.write(1, f"Getting embeddings\n".encode())
    os.write(1, f"API Key: {GOOGLE_API_KEY}\n".encode())
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    return embeddings
