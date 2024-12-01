# Usando uma imagem oficial do Python 3 como base
FROM python

# Atualize os pacotes e instale libncurses5 e libtinfo5 
RUN apt-get update && \
    apt-get upgrade && \
    # apt-get install -y libncurses5 libtinfo5 && \ 
    apt-get clean && \ 
    rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY requirements.txt /code
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP hello.py
ENV FLASK_ENV development
ENV FLASK_RUN_PORT 8000
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 8000

CMD ["flask", "run"]