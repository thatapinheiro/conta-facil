@echo off
echo 🧪 EXECUTANDO TESTES RAG
echo.
cd /d "%~dp0"
echo 1. Testando embeddings...
python debug_embeddings.py
echo.
echo 2. Testando serviço RAG...
python test_rag.py
echo.
echo ✅ Testes concluídos!
pause