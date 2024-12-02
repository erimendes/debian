


pip install gunicorn

gunicorn --workers 3 --bind 127.0.0.1:8000 app:app

sudo a2enmod proxy
sudo a2enmod proxy_http

# Copiar o arquivo de configuração do Flask para o diretório de sites do Apache
COPY flask-app.conf /etc/apache2/sites-available/

# Ativar o site
RUN a2ensite flask-app.conf

# Habilitar módulos necessários para o Apache
RUN a2enmod proxy_uwsgi
RUN a2enmod proxy

sudo systemctl restart apache2

http://192.168.15.100:8080/

