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

import sqlite3

from lib.bottle import route, get, post, run
from lib.markdown2 import markdown

@get('/wiki/<pagina>')
def wiki(pagina="principal"):
    return markdown('**Oi, como vai?**')

if __name__ == '__main__':
    run(host='localhost', port=8080)
