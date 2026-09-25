Zepto Support Assistant:
Overview

This module implements a document-grounded RAG-based AI support assistant using Zepto policy documents.

Workflow:
Policy Documents
      ↓
Chunking
      ↓
Embeddings
      ↓
ChromaDB
      ↓
LangGraph Intent Routing
      ↓
Retrieve / Direct Answer
      ↓
Pydantic Validation
      ↓
FastAPI API

Key Features:

Uses 8 Zepto policy documents covering delivery, returns, membership, tracking, cancellation, refunds, gift cards and customer support.
Generates local embeddings using Sentence Transformers (all-MiniLM-L6-v2).
Stores and retrieves document embeddings using ChromaDB.
Uses LangGraph with three nodes:
classify_intent
retrieve_and_answer
direct_answer
Uses deterministic MOCK_LLM mode for offline execution.
Retrieves the top relevant policy chunks for policy-related questions.
Returns structured responses using Pydantic with:
answer
sources
confidence
Provides a FastAPI /ask endpoint.
Includes a Dockerfile for local deployment.
RAG Architecture
User Query
    ↓
Intent Classification
    ↓
Policy Question?
   /       \
 Yes       No
 ↓          ↓
ChromaDB   Direct Answer
 ↓
Relevant Context
 ↓
Answer Generation
 ↓
Pydantic Response
Run
pip install -r requirements.txt
python ingestion.py
uvicorn main:app --host 0.0.0.0 --port 7860
Docker
docker build -t zepto-support-assistant .
docker run -p 7860:7860 zepto-support-assistant
Example Request
{
  "query": "What is the delivery fee for orders below INR 149?"
}
Files
docs/ – Zepto policy documents
ingestion.py – Document loading, chunking and embeddings
rag_graph.py – LangGraph workflow and retrieval
main.py – FastAPI application
Dockerfile – Container configuration
requirements.txt – Python dependencies
