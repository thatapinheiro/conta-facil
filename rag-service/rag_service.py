"""Serviço principal de RAG"""

from typing import List, Dict, Any
from embeddings import embedding_service
from knowledge_base import KNOWLEDGE_BASE, get_all_documents

class RAGService:
    def __init__(self, similarity_threshold: float = 0.3):
        self.similarity_threshold = similarity_threshold
        self.documents = get_all_documents()
        self.knowledge_map = {doc["conteudo"]: doc for doc in KNOWLEDGE_BASE}
    
    def search(self, query: str, top_k: int = 3) -> Dict[str, Any]:
        """Busca contexto relevante para a query"""
        # Busca por similaridade semântica
        similar_docs = embedding_service.similarity_search(
            query, self.documents, top_k=top_k
        )
        
        # Filtra por threshold de similaridade
        relevant_docs = [
            (doc, score) for doc, score in similar_docs 
            if score >= self.similarity_threshold
        ]
        
        if not relevant_docs:
            return {
                "context": "",
                "sources": [],
                "similarity_scores": []
            }
        
        # Constrói contexto
        context_parts = []
        sources = []
        scores = []
        
        for doc_content, score in relevant_docs:
            doc_info = self.knowledge_map[doc_content]
            context_parts.append(f"[{doc_info['categoria']}] {doc_content}")
            sources.append({
                "id": doc_info["id"],
                "categoria": doc_info["categoria"],
                "titulo": doc_info["titulo"]
            })
            scores.append(float(score))
        
        return {
            "context": "\n\n".join(context_parts),
            "sources": sources,
            "similarity_scores": scores
        }
    
    def get_context_for_llm(self, query: str) -> str:
        """Retorna contexto formatado para o LLM"""
        result = self.search(query)
        
        if not result["context"]:
            return ""
        
        return f"""CONTEXTO RELEVANTE:
{result["context"]}

Com base no contexto acima, responda à pergunta do usuário de forma precisa e detalhada."""

# Instância global
rag_service = RAGService()