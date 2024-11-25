#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from html import escape
import sys
import os
import datetime
import traceback
from flup.server.fcgi import WSGIServer
from urllib.parse import parse_qsl, parse_qs
import importlib.machinery

def returnError(environ, start_response, erro):
    """Retorna uma página de erro com detalhes do erro ocorrido."""
    msg = f'<p>Error: {erro}</p>'
    msg += f'<h1>FastCGI Environment: {os.getcwd()}</h1>'
    msg += '<table>'
    
    try:
        for k, v in sorted(environ.items()):
            msg += f'<tr><th>{escape(k)}</th><td>{escape(v)}</td></tr>'
    except Exception:
        msg += '<tr><th>X</th><td>X</td></tr>'
    
    msg += '</table>'
    length = len(msg)
    
    start_response('510 Internal Server Error', [('Content-type', 'text/html'), ('Content-Length', str(length))])
    return [msg.encode('utf-8')]


def main(environ, start_response):
    """Função principal que lida com a execução do código do servidor."""
    try:
        # Carregar o módulo dinamicamente
        loader = importlib.machinery.SourceFileLoader('operrun', './operrun.py')
        modoper = loader.load_module()

        return modoper.ret(environ, start_response)

    except Exception as e:  # captura todas as exceções de forma mais explícita
        tb = traceback.format_exc().replace('\n', '|')
        sys.stderr.write(f'{datetime.datetime.now()} ERROOPER: {os.getpid()} {tb}\n')

        return returnError(environ, start_response, str(e))


# Inicializa o servidor FastCGI
WSGIServer(main).run()
