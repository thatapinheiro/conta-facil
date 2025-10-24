"""API FastAPI para serviço RAG"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from rag_service import rag_service

app = FastAPI(title="RAG Service", version="1.0.0")

# CORS para integração com Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchRequest(BaseModel):
    query: str
    top_k: Optional[int] = 3

class SearchResponse(BaseModel):
    context: str
    sources: list
    similarity_scores: list

@app.get("/")
async def root():
    return {"message": "RAG Service is running"}

@app.post("/search", response_model=SearchResponse)
async def search_knowledge(request: SearchRequest):
    """Busca contexto relevante na base de conhecimento"""
    try:
        result = rag_service.search(request.query, request.top_k)
        return SearchResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/context")
async def get_context_for_llm(request: SearchRequest):
    """Retorna contexto formatado para LLM"""
    try:
        context = rag_service.get_context_for_llm(request.query)
        return {"context": context}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)