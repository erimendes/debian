from fastapi import FastAPI, HTTPException
import mysql.connector
from mysql.connector import Error
import os

app = FastAPI()

# Configuração do banco de dados a partir das variáveis de ambiente
db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST', 'db'),  # 'db' é o nome do serviço no docker-compose.yml
    'database': os.getenv('DB_NAME'),
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_general_ci'
}

@app.get("/")
async def read_root():
    try:
        # Adicione log antes de tentar a conexão
        # app.logger.info("Tentando conectar ao banco de dados com a configuração: %s", db_config)
        
        # Conectar ao banco de dados
        connection = mysql.connector.connect(
            **db_config
        )
        # connection = mysql.connector.connect(
        #     host='mariadb_container',
        #     user='root',
        #     password='senha_root',
        #     database='seu_banco',
        #     charset='utf8mb4',
        #     collation='utf8mb4_general_ci'
        # )
        # cursor = connection.cursor(dictionary=True)
        
        # # Executar consulta
        # cursor.execute("SELECT * FROM sua_tabela")
        # rows = cursor.fetchall()
        print("Connection successful!")
        
        return {"dados": "rows"}
    
    except Error as e:
        app.logger.error("Erro ao conectar ao banco de dados: %s", str(e))
        
    # return {"mensagem": f"Configuração do banco de dados: {db_config}"}

@app.get("/dados")
async def read_dados():
    try:
        # Adicione log antes de tentar a conexão
        # app.logger.info("Tentando conectar ao banco de dados com a configuração: %s", db_config)
        
        # Conectar ao banco de dados
        # connection = mysql.connector.connect(
        #     host="127.0.0.1",
        #     port=3306,
        #     user="root",
        #     password="senha_root"
        # )
        connection = mysql.connector.connect(
            **db_config
        )
        cursor = connection.cursor(dictionary=True)
        
        # # Executar consulta
        # cursor.execute("SELECT * FROM sua_tabela")
        # rows = cursor.fetchall()
        
        return {"dados": "rows"}
    
    except Error as e:
        app.logger.error("Erro ao conectar ao banco de dados: %s", str(e))
        # raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.get("/teste-conexao")
async def teste_conexao():
    try:
        # Adicione log antes de tentar a conexão
        # app.logger.info("Tentando conectar ao banco de dados com a configuração: %s", db_config)
        
        # Tentar conectar ao banco de dados
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            return {"mensagem": "Conexão bem-sucedida!"}
    except Error as e:
        app.logger.error("Erro ao conectar ao banco de dados: %s", str(e))
        return {"mensagem": f"Erro ao conectar ao banco de dados: {str(e)}"}
    finally:
        if connection.is_connected():
            connection.close()


# from fastapi import FastAPI, HTTPException
# import MySQLdb
# import os

# app = FastAPI()

# # Configuração do banco de dados a partir das variáveis de ambiente
# db_config = {
#     'user': os.getenv('DB_USER'),
#     'passwd': os.getenv('DB_PASSWORD'),
#     'host': os.getenv('DB_HOST', 'db'),  # 'db' é o nome do serviço no docker-compose.yml
#     'db': os.getenv('DB_NAME')
# }

# @app.get("/")
# async def read_root():
#     return {"mensagem": f"Configuração do banco de dados: {db_config}"}

# @app.get("/dados")
# async def read_dados():
#     try:
#         # Conectar ao banco de dados
#         connection = MySQLdb.connect(**db_config)
#         cursor = connection.cursor(MySQLdb.cursors.DictCursor)
        
#         # Executar consulta
#         cursor.execute("SELECT * FROM sua_tabela")
#         rows = cursor.fetchall()
        
#         return {"dados": rows}
    
#     except MySQLdb.Error as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
#     finally:
#         if 'connection' in locals() and connection.open:
#             cursor.close()
#             connection.close()

# @app.get("/teste-conexao")
# async def teste_conexao():
#     try:
#         # Tentar conectar ao banco de dados
#         connection = MySQLdb.connect(**db_config)
#         if connection:
#             return {"mensagem": "Conexão bem-sucedida!"}
#     except MySQLdb.Error as e:
#         return {"mensagem": f"Erro ao conectar ao banco de dados: {str(e)}"}
#     finally:
#         if 'connection' in locals() and connection.open:
#             connection.close()
