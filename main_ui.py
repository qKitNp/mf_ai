import streamlit as st 
from rag_pipe import query_rag


st.write("# Hello, welcome to the RAG Chatbot!")
query_text = st.text_input("## Enter your question:")

if st.button("Submit"):
    response_text = query_rag(query_text)
    st.write(response_text)

