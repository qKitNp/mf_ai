from langchain.vectorstores.chroma import Chroma
from embedding import get_embeddings
from langchain.schema.document import Document


def add_chroma(chunks :list[Document]):
    db=Chroma(
        persist_directory=CHROMA_PATH, 
        embedding_function=get_embeddings()
    )
    db.add_documents(new_chunks, ids=new_chunk_ids)
    db.persist()