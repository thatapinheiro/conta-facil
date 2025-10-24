"""Sistema de embeddings para RAG"""

from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple
import pickle
import os

class EmbeddingService:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.embeddings_cache = {}
        self.cache_file = "embeddings_cache.pkl"
        self._load_cache()
    
    def _load_cache(self):
        """Carrega cache de embeddings se existir"""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'rb') as f:
                    self.embeddings_cache = pickle.load(f)
            except:
                self.embeddings_cache = {}
    
    def _save_cache(self):
        """Salva cache de embeddings"""
        with open(self.cache_file, 'wb') as f:
            pickle.dump(self.embeddings_cache, f)
    
    def encode(self, texts: List[str]) -> np.ndarray:
        """Gera embeddings para lista de textos"""
        return self.model.encode(texts)
    
    def encode_single(self, text: str) -> np.ndarray:
        """Gera embedding para um texto único"""
        if text in self.embeddings_cache:
            return self.embeddings_cache[text]
        
        embedding = self.model.encode([text])[0]
        self.embeddings_cache[text] = embedding
        self._save_cache()
        return embedding
    
    def similarity_search(self, query: str, documents: List[str], top_k: int = 3) -> List[Tuple[str, float]]:
        """Busca documentos mais similares à query"""
        query_embedding = self.encode_single(query)
        doc_embeddings = [self.encode_single(doc) for doc in documents]
        
        similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
        
        # Ordena por similaridade (maior primeiro)
        doc_scores = list(zip(documents, similarities))
        doc_scores.sort(key=lambda x: x[1], reverse=True)
        
        return doc_scores[:top_k]

# Instância global
embedding_service = EmbeddingService()