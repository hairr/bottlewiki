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

from lib.bottle import route, get, post, run, redirect, request
from lib.bottle import jinja2_view as view
from lib.markdown2 import markdown


dados_view = {
    'site_url' : 'http://localhost:8080/'
}


@get('/')
@get('/wiki')
@get('/wiki/<pagina>')
@view('index.html')
def wiki(pagina="home"):
    dados_view['form'] = False
    dados_view['conteudo'] = ''
    dados_view['pagina'] = pagina
    pagina = './wiki/' + pagina + '.md'
    if (path.exists(pagina)):
        arquivo = open(pagina, 'r')
        dados_view['conteudo'] = markdown(arquivo.read())
        arquivo.close()
    else:
        dados_view['form'] = True
    return dados_view


@get('/editar/<pagina>')
@view('index.html')
def editar(pagina):
    dados_view['form'] = True
    dados_view['pagina'] = pagina
    dados_view['conteudo'] = ''
    pagina = './wiki/' + pagina + '.md'
    if (path.exists(pagina)):
        arquivo = open(pagina, 'r')
        dados_view['conteudo'] = arquivo.read()
        arquivo.close()
    return dados_view


@post('/salvar/<pagina>')
def salvar(pagina):
    conteudo = request.forms.get('texto')
    arquivo = open('./wiki/' + pagina + '.md', 'w')
    arquivo.write(conteudo)
    arquivo.close()
    redirect('/wiki/' + pagina)


@route('/<pagina>')
def redirecionar(pagina):
    redirect('/wiki/' + pagina)


if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)
