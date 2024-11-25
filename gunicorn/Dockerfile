# Usando uma imagem mais específica do Python, como a versão 3.11-slim
FROM python

# Definindo o diretório de trabalho no contêiner
WORKDIR /app

# Copiando o arquivo requirements.txt para o contêiner
COPY requirements.txt /app/

RUN pip install --upgrade pip --no-cache-dir

# Instalando as dependências a partir do arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código da aplicação para o contêiner
COPY . /app

# Expondo a porta 8000 para o Gunicorn
EXPOSE 8081

# Comando para rodar a aplicação com Gunicorn
# CMD	[“gunicorn”, ”-w” “4”,”myapp:app”,”--bind” “0.0.0.0:8000”]
CMD ["gunicorn", "main:app", "--port", "8001"]

