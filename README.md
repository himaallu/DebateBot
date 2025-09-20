# DebateBot – RAG-Powered AI Debate Generator

**Tech Stack:** Streamlit | LangChain | Gemini API | FAISS | HuggingFace Embeddings

## Overview
DebateBot is an AI system that generates **structured debates (Pro vs. Con)** from uploaded policy PDFs using **Retrieval-Augmented Generation (RAG)**. It retrieves relevant context from documents, feeds it into LLM prompts, and produces debate arguments grounded in the source material.

## Features
- Upload PDF reports and extract key arguments.
- RAG with **FAISS** + **HuggingFace embeddings**.
- AI-generated **Pro vs. Con debates** using **Gemini API**.
- Moderator summary combining both perspectives.
- Interactive **Streamlit web app**.

## How It Works
1. **PDF upload** → split into chunks → generate embeddings → store in FAISS vectorstore.  
2. **User enters debate topic** → retrieve top-k relevant chunks → send to Gemini LLM.  
3. **Generate Pro & Con arguments**, plus **moderator summary**.
