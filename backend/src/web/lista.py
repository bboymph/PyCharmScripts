# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web.rest.rest import Usuario

def index(_write_tmpl):

    class Aluno(object):
        def __init__(self, id='', nome='', sobrenome='', email=''):
            self.id= id
            self.nome = nome
            self.sobrenome = sobrenome
            self.email = email
    #alunos = [Aluno(nome) for nome in ('PyPrático','Objetos Pythônicos','Python para quem sabe Python')]
    #dct = {'lista_alunos': alunos}

    query = Usuario.query().order(Usuario.nome)
    alunos = query.fetch()
    dct = {'lista_alunos': alunos}

    _write_tmpl('/templates/lista.html', dct)

