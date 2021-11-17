
import hashlib
from datetime import datetime

from Controllers.Db import DB
try:
    from Controllers.credentials import _host, _dbname, _username, _password
except:
    print('[!] - CREDENTIALS')

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
        self.result = []

    def validarData(self, data = ''):
        result =  None
        try:
            result = datetime.strptime(data, '%Y-%m-%d').date()
            # result = True
        except:
            result = False
        
        return result

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
        self.result = []
        self.db.toConnect()

        query = "SELECT id, nome, cod_ubs FROM ubs"
        result = self.db.fetchAll(query)

        if result == None:
            aux = False
        else:
            self.result = result
            aux =  True

        self.db.disconnect()

        return aux


    def getListACS(self):
        aux = None
        self.result = []
        self.db.toConnect()

        query = "SELECT id, nome, cod_ma FROM acs"
        result = self.db.fetchAll(query)

        if result == None:
            aux = False
        else:
            self.result = result
            aux =  True

        self.db.disconnect()

        return aux

    def getListBatchVaccine(self):
        aux = None
        self.result = []
        self.db.toConnect()

        query = '''SELECT l.id, l.lote, v.nome,
                DATE_FORMAT(l.fabricacao,'%Y-%m-%d'), DATE_FORMAT(l.validade,'%Y-%m-%d')
                FROM lote_vacina AS l INNER JOIN vacina AS v
                ON l.fk_vacina = v.id '''
        result = self.db.fetchAll(query)

        if result == None:
            aux = False
        else:
            self.result = result
            aux =  True

        self.db.disconnect()

        return aux

    def getListVaccine(self):
        aux = None
        self.result = []
        self.db.toConnect()

        query = '''SELECT v.id, v.nome, v.reforco, l.nome
                FROM vacina AS v INNER JOIN laboratorio
                AS l ON v.laboratorio = l.id'''
        result = self.db.fetchAll(query)

        if result == None:
            aux = False
        else:
            self.result = result
            aux =  True


        self.db.disconnect()

        return aux


    def getListLaboratory(self):
        aux = None
        self.result = []
        self.db.toConnect()

        query = "SELECT id, nome FROM laboratorio"
        result = self.db.fetchAll(query)

        if result == None:
            aux = False
        else:
            self.result = result
            aux =  True


        self.db.disconnect()

        return aux

    def getListCommunity(self):
        aux = None
        self.result = []
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
            self.result = result
            aux =  True


        self.db.disconnect()

        return aux


    # CADASTRAR

    def cadastrar_ubs(self, cod, nome):
        self.db.toConnect()
    
        query = 'INSERT INTO ubs (cod_ubs, nome) VALUES (%s, %s)'
        result = self.db.cursor(query, (cod, nome))

        self.db.disconnect()
        return result

    def cadastrar_acs(self, cod, nome):
        self.db.toConnect()
    
        query = 'INSERT INTO acs (cod_ma, nome) VALUES (%s, %s)'
        result = self.db.cursor(query, (cod, nome))

        self.db.disconnect()
        return result

    def cadastrar_lote(self, fk_vacina, lote, fabricacao, validade):
        self.db.toConnect()

        result = None

        query = 'SELECT id FROM vacina WHERE id =  ' + fk_vacina
        result = self.db.fetchOne(query)

        if result:
            query = 'INSERT INTO lote_vacina (fk_vacina, lote, fabricacao, validade) VALUES (%s, %s, %s,%s)'
            result = self.db.cursor(query, (fk_vacina, lote, fabricacao, validade))
        else:
            result = -1 # LOTE NÃO EXISTE

        self.db.disconnect()
        return result

    def cadastrar_vacina(self, nome, reforco, laboratorio):
        self.db.toConnect()

        result = None

        query = 'SELECT id FROM laboratorio WHERE id =  ' + laboratorio
        result = self.db.fetchOne(query)

        if result:
            query = 'INSERT INTO vacina (nome, reforco, laboratorio) VALUES (%s, %s, %s)'
            result = self.db.cursor(query, (nome, reforco, laboratorio))
        else:
            result = -1 # LABORATORIO NÃO EXISTE

        self.db.disconnect()
        return result


    def cadastrar_laboratorio(self, nome):
        self.db.toConnect()
        result = None
        
        query = 'INSERT INTO laboratorio (id, nome) VALUES (%s,%s)'
        result = self.db.cursor(query, ('NULL', nome))
       
        self.db.disconnect()
        return result

