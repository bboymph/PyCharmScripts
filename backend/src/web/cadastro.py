# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web.user.Aluno import Aluno
from web.rest.rest import Usuario
def index(_write_tmpl):

    query = Aluno.listar()
    alunos = query.fetch()
    dct = {'lista_alunos': alunos}

    _write_tmpl('/templates/cadastro.html', dct)

def cadastrar(_handler, _write_tmpl, nome, sobrenome, email, id):
    Usuario.cadastrar(nome, sobrenome, email, id)
    _handler.redirect('/cadastro')
    #_write_tmpl('/templates/cadastro.html')


