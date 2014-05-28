# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb

class Usuario(ndb.Model):
    nome = ndb.StringProperty()
    sobrenome = ndb.StringProperty()
    email = ndb.StringProperty()
    id = ndb.StringProperty()

    @classmethod
    def cadastrar(cls, nome, sobrenome, email, id):
        Usuario(nome=nome, sobrenome=sobrenome, email=email, id=id).put()


def logar(login, pwd):
    query = Usuario.query(Usuario.login == login, Usuario.pwd == pwd)
    if query.fetch():
        usuario = query.get()
        setattr(usuario, 'logged', True)
        usuario.put()
        return True
    return False

def get_all_users(_write):
    users = Usuario.query().fetch()
    users = [user.to_dict() for user in users]
    _write(json.dumps(users))

def remove_user(nome):
    user = Usuario.query(Usuario.nome == nome).get()
    if user:
        user.key.delete()

def edit_user(id, nome, email):
    user = Usuario.query(Usuario.id == id).get()
    if user:
        user.nome = nome
        #user.sobrenome = sobrenome
        user.email = email
        user.put()
    else:
        user = Usuario(nome=nome, email=email)
        user.put()

