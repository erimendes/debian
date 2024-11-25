# Usando uma imagem oficial do Python como base
FROM python
# Definindo o diretório de trabalho no contêiner
WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip --no-cache-dir

# Instalando as dependências a partir do arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install "uvicorn[standard]"

# Copiando o código da aplicação para o contêiner
COPY . /app

# Expondo a porta em que o Uvicorn irá rodar
EXPOSE 8080

# Usando o comando uvicorn para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
