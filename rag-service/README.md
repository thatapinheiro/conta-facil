# 🤖 Serviço RAG - Consultor Contábil

Serviço Python para Retrieval-Augmented Generation integrado ao sistema Node.js.

## 🚀 Instalação

```bash
cd rag-service
pip install -r requirements.txt
```

## ▶️ Execução

### Windows
```bash
start.bat
```

### Linux/Mac
```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📡 API Endpoints

### POST /search
Busca contexto relevante na base de conhecimento
```json
{
  "query": "Como calcular MEI?",
  "top_k": 3
}
```

### POST /context
Retorna contexto formatado para LLM
```json
{
  "query": "Limites do Simples Nacional"
}
```

### GET /health
Health check do serviço

## 🔧 Configuração

O serviço roda na porta 8000 e aceita conexões do Next.js (porta 3000).

## 📚 Base de Conhecimento

Localizada em `knowledge_base.py` com informações sobre:
- MEI
- Simples Nacional  
- Lucro Presumido
- ICMS/ISS
- Folha de Pagamento
- Prazos Tributários