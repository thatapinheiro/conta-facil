# 🧪 Testes RAG

Diretório com scripts para testar o funcionamento do sistema RAG.

## 📁 Arquivos

### `test_rag.py`
Teste completo do serviço RAG via API:
- Testa endpoints `/search` e `/context`
- Verifica categorias e similaridade
- Valida termos específicos no contexto

### `debug_embeddings.py`
Debug do sistema de embeddings:
- Testa geração de embeddings
- Verifica busca por similaridade
- Analisa qualidade dos resultados

### `run_tests.bat`
Script para executar todos os testes automaticamente.

## ▶️ Como Executar

### Todos os testes:
```bash
cd testes
run_tests.bat
```

### Testes individuais:
```bash
cd testes
python test_rag.py
python debug_embeddings.py
```

## 📊 Interpretação dos Resultados

### ✅ RAG Funcionando:
- Similaridade > 0.3 para perguntas relevantes
- Categorias corretas encontradas
- Termos específicos no contexto

### ❌ RAG com Problemas:
- Similaridade baixa (< 0.3)
- Categorias incorretas
- Contexto vazio ou irrelevante

## 🔗 Teste via Web

Acesse: `http://localhost:3000/api/test-rag`