__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st 
import os
from rag_pipe import query_rag

# Custom CSS for chat interface (optional)
st.markdown("""
<style>
    /* Main container padding */
    .stApp {
        padding: 1rem;
    }
    
    /* Chat message styling */
    .chat-message {
        padding: 1rem;
        border-radius: 1rem;
        margin-bottom: 1rem;
        display: flex;
        max-width: 80%;
    }
    
    .user-message {
        background-color: #3b3b3b;
        color: white;
        margin-left: auto;
    }
    
    .assistant-message {
        background-color: #2b2b2b;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.markdown("# 🔍 Mutual Fund AI Assistant")

# Display chat messages in order (oldest on top)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Use st.chat_input() for user prompt
if prompt := st.chat_input("Ask me anything about mutual funds..."):
    # Add user prompt to chat history and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get assistant response
    with st.spinner("Searching..."):
        assistant_response = query_rag(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
    
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})