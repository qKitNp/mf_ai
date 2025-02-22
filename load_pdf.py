from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader

def load_pdf(file_path):
    pdf_loader = PyPDFDirectoryLoader(file_path)
    pdf_loader.load()
    return pdf_loader.load()

if __name__ == '__main__':
    # for i in range(10):``
    print(load_pdf('pdfs').range)