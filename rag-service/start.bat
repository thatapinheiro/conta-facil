@echo off
echo Iniciando serviço RAG...
cd /d "%~dp0"
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000