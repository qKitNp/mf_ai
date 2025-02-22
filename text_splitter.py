from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from load_pdf import load_pdf

def split_text(documents: list[Document]):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=24000,
        chunk_overlap=4000,
        length_function=len,
        is_separator_regex=False
    )
    return splitter.split_documents(documents)

def get_chuck_id(chunk):
    source = chunk.metadata.get("source")
    page = chunk.metadata.get("page")
    return f"{source}:{page}"


if __name__ == '__main__':
    documents = load_pdf('pdfs')
    print("PRINTING THE CHUNCK")
    last_page_id = None
    current_chunk_index = 0
    for chunk in split_text(documents):
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}:{current_chunk_index}"
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        current_page_id = f"{source}:{page}:{current_chunk_index}"        
        print(current_page_id)
        last_page_id = current_page_id