# Usar a imagem base oficial do Python
FROM python

# Instalar dependências do sistema RUN apt-get update && apt-get install -y \ gcc \ libmariadb-dev \ && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y \ 
    gcc \ 
    libmariadb-dev \ 
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o conteúdo do projeto para o contêiner
COPY . .

# Comando para rodar o Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
