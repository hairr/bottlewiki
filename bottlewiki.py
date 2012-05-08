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

from lib.bottle import route, get, post, run, template
from lib.markdown2 import markdown

dados_view = {
    'site_url' : 'http://localhost:8080/'
}


@get('/')
@get('/wiki')
@get('/wiki/<pagina>')
def wiki(pagina="home"):
    dados_view['pagina'] = pagina
    pagina = './wiki/' + pagina + '.md'
    if (path.exists(pagina)):
        arquivo = open(pagina, 'r')
        conteudo = markdown(arquivo.read())
    else:
        conteudo = template('templates/form.html', dados_view)
    conteudo = template('templates/cabecalho.html', dados_view) + conteudo
    conteudo += template('templates/rodape.html')
    return conteudo

if __name__ == '__main__':
    run(host='localhost', port=8080)
