# 🔍 Mutual Fund AI Assistant

An AI-powered chat interface that helps users understand mutual fund information through natural conversation. Built with Streamlit, LangChain, and Google's Gemini model.

## 🚀 Features

- Interactive chat interface
- RAG (Retrieval Augmented Generation) implementation
- Real-time streaming responses
- PDF document processing capabilities
- Persistent chat history
- Custom styling

## 🛠️ Prerequisites

- Python 3.11 or higher
- Poetry (optional but recommended)
- Google Gemini API key
- Cohere API key

## 📦 Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd mf_ai
```

2. Set up a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## ⚙️ Local Development Setup

1. Create necessary directories:
```bash
mkdir .streamlit pdfs chroma
```

2. Create and configure secrets file:
```bash
mkdir -p .streamlit
touch .streamlit/secrets.toml
```

3. Add your API keys to `.streamlit/secrets.toml`:
```toml
# filepath: .streamlit/secrets.toml
GOOGLE_API_KEY = "your-gemini-api-key"
COHERE_KEY = "your-cohere-api-key"
```

4. Add `.env` file for environment variables:
```bash
touch .env
```

5. Configure `.env`:
```bash
# filepath: .env
GOOGLE_API_KEY=your-gemini-api-key
COHERE_KEY=your-cohere-api-key
```

## 📄 Document Processing

1. Place your mutual fund PDF documents in the `pdfs` directory

2. Process documents and create vector database:
```bash
python populate_db.py
```

To reset the database:
```bash
python populate_db.py --reset
```

## 🚀 Running the Application

1. Start the Streamlit server:
```bash
streamlit run main_ui.py
```

2. Access the application at `http://localhost:8501`

## 🗂️ Project Structure

```
mf_ai/
├── .streamlit/
│   └── secrets.toml
├── pdfs/              # PDF documents
├── chroma/            # Vector database
├── main_ui.py         # Streamlit interface
├── rag_pipe.py        # RAG implementation
├── embedding.py       # Embedding config
├── populate_db.py     # DB population
├── load_pdf.py        # PDF processing
└── requirements.txt
```

## 🔒 Security

Add these to your `.gitignore`:
```gitignore
# filepath: .gitignore
.env
.streamlit/
__pycache__/
*.pyc
.venv/
chroma/
```

## 🐛 Troubleshooting

Common issues and solutions:

1. **SQLite errors**: Install pysqlite3-binary:
```bash
pip install pysqlite3-binary
```

2. **Chromadb version conflicts**: Use specific version:
```bash
pip install chromadb==0.4.18
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

