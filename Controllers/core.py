
import hashlib

from Controllers.Db import DB
from Controllers.credentials import _host, _dbname, _username, _password

from Controllers.login import Login


def MD5hash(arg):
    result = ""
    if not(arg == ""):
        str = hashlib.md5()
        str.update(arg.encode('utf-8'))
        result = str.hexdigest()
    return result

class Core:
    def __init__(self) -> None:
        self.db = DB(_host, _dbname, _username, _password)

    def login(self,email, password):
        aux = None

        password = MD5hash(password)

        self.db.toConnect()
        query = "SELECT id FROM usuario WHERE email = '" + email + "' AND senha = '" + password + "'"
        result = self.db.fetchOne(query)

        if result == None:
            aux = False
        else:
            self.id = result[0]
            print(self.id)
            aux =  True

        self.db.disconnect()

        return aux
    
    def getListUBS(self):
        aux = None
        self.db.toConnect()

        query = "SELECT id, nome, cod_ubs FROM ubs"
        result = self.db.fetchAll(query)

        if result == None:
            aux = False
        else:
            for c in result:
                print("ID USER:", c)
            aux =  True


        self.db.disconnect()

        return aux


    def getListACS(self):
        aux = None
        self.db.toConnect()

        query = "SELECT id, nome, cod_ma FROM acs"
        result = self.db.fetchAll(query)

        if result == None:
            aux = False
        else:
            for c in result:
                print(c)
            aux =  True


        self.db.disconnect()

        return aux

    def getListBatchVaccine(self):
        aux = None
        self.db.toConnect()

        query = '''SELECT l.id, l.lote, v.nome,
                DATE_FORMAT(l.fabricacao,'%Y-%m-%d'), DATE_FORMAT(l.validade,'%Y-%m-%d')
                FROM lote_vacina AS l INNER JOIN vacina AS v
                ON l.fk_vacina = v.id '''
        result = self.db.fetchAll(query)

        if result == None:
            aux = False
        else:
            for c in result:
                print(c)
            aux =  True


        self.db.disconnect()

        return aux

    def getListVaccine(self):
        aux = None
        self.db.toConnect()

        query = '''SELECT v.id, v.nome, v.reforco, l.nome
                FROM vacina AS v INNER JOIN laboratorio
                AS l ON v.laboratorio = l.id'''
        result = self.db.fetchAll(query)

        if result == None:
            aux = False
        else:
            for c in result:
                print(c)
            aux =  True


        self.db.disconnect()

        return aux


    def getListLaboratory(self):
        aux = None
        self.db.toConnect()

        query = "SELECT id, nome FROM laboratorio"
        result = self.db.fetchAll(query)

        if result == None:
            aux = False
        else:
            for c in result:
                print(c)
            aux =  True


        self.db.disconnect()

        return aux

    def getListCommunity(self):
        aux = None
        self.db.toConnect()

        query = '''SELECT c.id, c.nome, c.cpf, c.num_sus, c.status_1dose, c.status_2dose,
                DATE_FORMAT(c.data_1dose,'%Y-%m-%d'), DATE_FORMAT(c.data_2dose,'%Y-%m-%d'),
                v.nome
                FROM comunitario AS c INNER JOIN vacina
                AS v ON c.fk_vacina_tipo = v.id'''
        result = self.db.fetchAll(query)

        if result == None:
            aux = False
        else:
            for c in result:
                print(c)
            aux =  True


        self.db.disconnect()

        return aux