import os
from PyPDF2 import PdfReader
# Old, working version for langchain 0.1.16
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings


# PDF loader
def load_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text

# Split docs into chunks
def split_documents(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    return splitter.split_text(text)

# Build FAISS vectorstore
def build_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_texts(chunks, embedding=embeddings)

# Retrieve context
def retrieve_context(query, vs, k=3):
    docs = vs.similarity_search(query, k=k)
    return "\n".join([d.page_content for d in docs])
