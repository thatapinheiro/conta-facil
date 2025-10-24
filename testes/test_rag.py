"""Script para testar o funcionamento do RAG"""

import requests
import json
from typing import Dict, Any

def test_rag_service():
    """Testa o serviço RAG com perguntas específicas"""
    
    base_url = "http://localhost:8000"
    
    # Perguntas de teste com respostas esperadas
    test_cases = [
        {
            "pergunta": "Qual o limite do MEI?",
            "categoria_esperada": "MEI",
            "deve_conter": ["81.000", "DAS", "67"]
        },
        {
            "pergunta": "Como calcular Simples Nacional?",
            "categoria_esperada": "Simples Nacional", 
            "deve_conter": ["4.800.000", "anexo", "RBT12"]
        },
        {
            "pergunta": "Prazos de PIS e COFINS",
            "categoria_esperada": "Prazos",
            "deve_conter": ["dia 25", "INSS", "dia 20"]
        },
        {
            "pergunta": "Como calcular ICMS por dentro?",
            "categoria_esperada": "ICMS",
            "deve_conter": ["1 - alíquota", "DIFAL"]
        },
        {
            "pergunta": "Pergunta sem contexto relevante sobre futebol",
            "categoria_esperada": None,
            "deve_conter": []
        }
    ]
    
    print("🧪 TESTANDO SERVIÇO RAG")
    print("=" * 50)
    
    # Teste de saúde
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Serviço RAG está online")
        else:
            print("❌ Serviço RAG offline")
            return
    except:
        print("❌ Não foi possível conectar ao serviço RAG")
        return
    
    # Testes de busca
    for i, test in enumerate(test_cases, 1):
        print(f"\n📝 TESTE {i}: {test['pergunta']}")
        print("-" * 40)
        
        try:
            # Teste endpoint /search
            response = requests.post(
                f"{base_url}/search",
                json={"query": test["pergunta"], "top_k": 3}
            )
            
            if response.status_code == 200:
                result = response.json()
                
                print(f"📊 Similaridade: {result['similarity_scores']}")
                print(f"📚 Fontes encontradas: {len(result['sources'])}")
                
                if result['sources']:
                    for source in result['sources']:
                        print(f"   - {source['categoria']}: {source['titulo']}")
                    
                    # Verifica se encontrou a categoria esperada
                    if test['categoria_esperada']:
                        categorias_encontradas = [s['categoria'] for s in result['sources']]
                        if test['categoria_esperada'] in categorias_encontradas:
                            print("✅ Categoria correta encontrada")
                        else:
                            print(f"⚠️  Categoria esperada '{test['categoria_esperada']}' não encontrada")
                    
                    # Verifica conteúdo
                    contexto = result['context'].lower()
                    for termo in test['deve_conter']:
                        if termo.lower() in contexto:
                            print(f"✅ Termo '{termo}' encontrado no contexto")
                        else:
                            print(f"❌ Termo '{termo}' NÃO encontrado")
                else:
                    print("ℹ️  Nenhum contexto relevante encontrado")
                    if test['categoria_esperada'] is None:
                        print("✅ Comportamento esperado (pergunta irrelevante)")
                    else:
                        print("❌ Deveria ter encontrado contexto relevante")
            
            else:
                print(f"❌ Erro na busca: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Erro no teste: {e}")
    
    print("\n" + "=" * 50)
    print("🏁 TESTES CONCLUÍDOS")

def test_context_endpoint():
    """Testa especificamente o endpoint de contexto para LLM"""
    
    print("\n🤖 TESTANDO CONTEXTO PARA LLM")
    print("=" * 50)
    
    pergunta = "Como calcular o DAS do MEI?"
    
    try:
        response = requests.post(
            "http://localhost:8000/context",
            json={"query": pergunta}
        )
        
        if response.status_code == 200:
            result = response.json()
            contexto = result['context']
            
            if contexto:
                print("✅ Contexto gerado com sucesso")
                print(f"📏 Tamanho do contexto: {len(contexto)} caracteres")
                print("\n📄 CONTEXTO GERADO:")
                print("-" * 30)
                print(contexto)
                print("-" * 30)
                
                # Verifica se contém informações relevantes
                if "MEI" in contexto and "DAS" in contexto:
                    print("✅ Contexto contém informações relevantes sobre MEI e DAS")
                else:
                    print("⚠️  Contexto pode não estar totalmente relevante")
            else:
                print("❌ Nenhum contexto foi gerado")
        else:
            print(f"❌ Erro: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Erro no teste: {e}")

if __name__ == "__main__":
    test_rag_service()
    test_context_endpoint()