#!/usr/bin/env python3
#
# Bottle Wiki
#
# Uma Wiki simples escrita em Python 3 e Bottle
# Utilize a linguagem de marcação Markdown para elaborar suas páginas
#
# Autor: Evaldo Junior <junior@casoft.info>
#
# Versão 0.1

from os import path

from lib.bottle import route, get, post, run
from lib.markdown2 import markdown

@get('/')
@get('/wiki')
@get('/wiki/<pagina>')
def wiki(pagina="home"):
    pagina = './wiki/' + pagina + '.md'
    if (path.exists(pagina)):
        conteudo = open(pagina, 'r')
        return markdown(conteudo.read())

if __name__ == '__main__':
    run(host='localhost', port=8080)
