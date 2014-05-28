# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web.user.Aluno import Aluno
from web.rest.rest import Usuario
def index(_write_tmpl):

    query = Aluno.listar()
    alunos = query.fetch()
    dct = {'lista_alunos': alunos}

    _write_tmpl('/templates/cadastro2.html', dct)

def cadastrar(_handler,_write_tmpl, nome, sobrenome, email, senha):
    Usuario.cadastrar(nome, sobrenome, email)
    _handler.redirect('/cadastro2')
    #_write_tmpl('/templates/cadastro.html')


