# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb

class Aluno(ndb.Model):
    nome = ndb.StringProperty()
    sobrenome = ndb.StringProperty()
    email = ndb.StringProperty()
    senha = ndb.StringProperty()

    @classmethod
    def cadastrar(cls, nome, sobrenome, email, senha):
        aluno = Aluno(nome=nome, sobrenome=sobrenome, email=email, senha=senha)
        aluno.put()

    @classmethod
    def listar(cls):
        return cls.query()


