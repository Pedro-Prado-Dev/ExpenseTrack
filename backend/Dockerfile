# Use uma imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho como /app
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Copie o restante do código para o contêiner
COPY . .

# Exponha a porta 5000
EXPOSE 5000

# Comando para executar o aplicativo Flask
CMD ["python", "app.py"]
