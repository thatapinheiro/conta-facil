@echo off
echo Corrigindo instalação...
pip uninstall sentence-transformers huggingface-hub transformers -y
pip install --upgrade pip
pip install -r requirements.txt
echo Instalação corrigida!
pause