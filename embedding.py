from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

GOOGLE_API_KEY = st.secrets["general"]["API_KEY"]

def get_embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    return embeddings
