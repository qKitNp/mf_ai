__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st 
import os
from rag_pipe import query_rag


st.write("# Hello, welcome to the RAG Chatbot!")
query_text = st.text_input("## Enter your question:")

if st.button("Submit"):
    os.write(1, f"Button Clicked\n".encode())
    response_text = query_rag(query_text)
    st.write(response_text)

