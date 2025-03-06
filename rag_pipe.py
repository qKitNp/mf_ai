__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import argparse
# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import time
from embedding import get_embeddings, GOOGLE_API_KEY, get_cohere_embeddings

CHROMA_PATH = "chroma"



PROMPT_TEMPLATE = """
You are a knowledgeable and friendly financial information assistant. Your role is to help people understand mutual fund information using the context provided to you. You should engage naturally with users while maintaining complete accuracy based on the available information.

Instructions for information handling:
1. Use ONLY the information provided in the context
2. Maintain accuracy while speaking conversationally
3. If information is not available in the context, clearly say so
4. Present numerical data exactly as shown in the context without rounding unless requested

Communication style:
- Engage naturally as a knowledgeable financial professional would
- Avoid starting responses with phrases like "Based on the provided text"
- Use clear, approachable language while maintaining accuracy
- Break down complex information into digestible pieces
- Add brief transitions between different pieces of information
- Use natural connecting phrases like "I see that", "According to the information", "I noticed that", "The data shows"

When responding:
1. Lead with the most relevant information to answer the question
2. Organize information in a logical, flowing manner
3. Use appropriate context when presenting numbers or data
4. Include relevant caveats or important notes naturally in the conversation

Context: {context}

Question: {question}

Remember to:
- Stay within the scope of provided information
- Be direct and natural in your responses
- Maintain accuracy while being conversational
- Clearly indicate if any requested information is not available
"""


def main():
    # Create CLI.
    while True:
        query_text = input("Enter your question: ")
        query_rag(query_text)


def query_rag(query_text: str):
    # os.write(1, f"Querying RAG with {query_text}\n".encode())
    # Prepare the DB.
    embedding_function = get_cohere_embeddings()
    # os.write(1, f"Got embeddings\n".encode())
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    #os.write(1, f"Got DB\n".encode())

    # os.write(1, f"Searching DB\n".encode())
    results = db.similarity_search_with_score(query_text, k=20)
    # os.write(1, f"Got results\n".encode())
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # os.write(1, f"Prepared prompt\n".encode())
    
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=GOOGLE_API_KEY)
    # os.write(1, f"Selected Model\n".encode())
    
    # Calling without stream parameter.
    full_response = model.invoke(prompt)
    # Extract content from the AIMessage object.
    full_text = full_response.content
    # Simulate streaming by splitting the full_text into chunks.
    words = full_text.split()
    chunk = ""
    for word in words:
        chunk += word + " "
        # yield a chunk every 10 words.
        if len(chunk.split()) >= 10:
            yield chunk
            chunk = ""
            time.sleep(0.1)  # small delay to simulate streaming
    if chunk:
        yield chunk


if __name__ == "__main__":
    main()