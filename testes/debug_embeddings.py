"""Script para debugar embeddings e similaridade"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'rag-service'))

from embeddings import embedding_service
from knowledge_base import get_all_documents, KNOWLEDGE_BASE
import numpy as np

def debug_embeddings():
    """Debug do sistema de embeddings"""
    
    print("🔍 DEBUG EMBEDDINGS")
    print("=" * 40)
    
    # Teste básico de embedding
    test_text = "Como calcular MEI?"
    embedding = embedding_service.encode_single(test_text)
    
    print(f"📝 Texto teste: '{test_text}'")
    print(f"📊 Embedding shape: {embedding.shape}")
    print(f"📈 Embedding sample: {embedding[:5]}")
    
    # Teste de similaridade
    documents = get_all_documents()
    print(f"\n📚 Total de documentos: {len(documents)}")
    
    # Busca similaridade
    results = embedding_service.similarity_search(test_text, documents, top_k=5)
    
    print(f"\n🎯 TOP 5 RESULTADOS PARA: '{test_text}'")
    print("-" * 50)
    
    for i, (doc, score) in enumerate(results, 1):
        # Encontra o documento original
        doc_info = next((d for d in KNOWLEDGE_BASE if d["conteudo"] == doc), None)
        categoria = doc_info["categoria"] if doc_info else "Desconhecida"
        
        print(f"{i}. Similaridade: {score:.4f}")
        print(f"   Categoria: {categoria}")
        print(f"   Conteúdo: {doc[:100]}...")
        print()
    
    # Teste com diferentes queries
    test_queries = [
        "MEI limite anual",
        "Simples Nacional anexo",
        "ICMS cálculo",
        "Prazos vencimento",
        "Futebol Copa do Mundo"  # Query irrelevante
    ]
    
    print("\n🧪 TESTE DE MÚLTIPLAS QUERIES")
    print("=" * 50)
    
    for query in test_queries:
        results = embedding_service.similarity_search(query, documents, top_k=3)
        best_score = results[0][1] if results else 0
        
        print(f"Query: '{query}'")
        print(f"Melhor similaridade: {best_score:.4f}")
        
        if best_score > 0.3:
            print("✅ Contexto relevante encontrado")
        else:
            print("❌ Nenhum contexto relevante")
        print()

if __name__ == "__main__":
    debug_embeddings()