import unittest
from backend.teste.base import GAETestCase
from web.rest import rest
from web.rest.rest import Usuario

from web import cadastro

__author__ = 'Rodrigo Brito'


class RestTest(GAETestCase):
    def test_cadastrar(self):
        #rest.cadastrar(Usuario('Rodrigo','Brito','rodrigo@britoinf@gmail.com','1234'))
        rest.Usuario.cadastrar('Rodrigo','Brito','rodrigo@britoinf@gmail.com','1234')
        lista = Usuario.query().fetch()
        usuario = lista[0]
        self.assertEquals(1,len(lista))
        self.assertEquals('Rodrigo',usuario.nome)

    def test_remover(self):
        rest.Usuario.cadastrar('Rodrigo','Brito','rodrigo.britoinf@gmail.com','1234'),
        rest.Usuario.cadastrar('Rodrigo2','Brito','rodrigo.britoinf2@gmail.com','222')
        rest.remove_user('Rodrigo')
        lista = Usuario.query().fetch()
        self.assertEquals(1,len(lista))

    def test_listar(self):
        rest.Usuario.cadastrar('Rodrigo','Brito','rodrigo.britoinf@gmail.com','123'),
        rest.edit_user('123', 'MudeiNome','MudeiEmail')
        lista = Usuario.query().fetch()
        user = lista[0]
        self.assertNotEqual('Rodrigo',user.nome)






