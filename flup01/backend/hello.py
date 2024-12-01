import os
from flask import Flask, request
import mysql.connector
import logging

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuração do banco de dados a partir das variáveis de ambiente
db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST', 'mariadb_container'),  # 'mariadb_container' é o nome do serviço no docker-compose.yml
    'database': os.getenv('DB_NAME'),
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_general_ci'
}

class DBManager:
    def __init__(self, database=None, host=None, user=None, password=None):
        if database:
            db_config['database'] = database
        if host:
            db_config['host'] = host
        if user:
            db_config['user'] = user
        if password:
            db_config['password'] = password

        # Log da configuração do banco de dados
        logger.info(f'Database config: {db_config}')

        # Conectar ao banco de dados
        try:
            self.connection = mysql.connector.connect(**db_config)
            self.cursor = self.connection.cursor()
            logger.info('Database connection established successfully')
        except mysql.connector.Error as err:
            logger.error(f'Error connecting to database: {err}')

    def populate_db(self):
        try:
            self.cursor.execute('DROP TABLE IF EXISTS blog')
            self.cursor.execute('CREATE TABLE blog (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))')
            self.cursor.executemany(
                'INSERT INTO blog (id, title) VALUES (%s, %s);',
                [(i, f'Blog post #{i}') for i in range(1, 5)]
            )
            self.connection.commit()
            logger.info('Database populated successfully')
        except mysql.connector.Error as err:
            logger.error(f'Error populating database: {err}')

    def query_titles(self):
        try:
            self.cursor.execute('SELECT title FROM blog')
            result = [c[0] for c in self.cursor]
            logger.info('Titles queried successfully')
            return result
        except mysql.connector.Error as err:
            logger.error(f'Error querying titles: {err}')
            return []

server = Flask(__name__)
conn = None

@server.route('/')
def list_blog():
    global conn
    if not conn:
        conn = DBManager(
            password=os.getenv('DB_PASSWORD')  # Usando a variável de ambiente diretamente
        )
        conn.populate_db()
    rec = conn.query_titles()

    response = ''
    for title in rec:
        response += f'<div>Hello {title}</div>'
    return response

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8000)
