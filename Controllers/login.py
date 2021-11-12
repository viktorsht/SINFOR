import hashlib

from Controllers.Db import DB
from Controllers.credentials import _host, _dbname, _username, _password


def MD5hash(arg):
    result = ""
    if not(arg == ""):
        str = hashlib.md5()
        str.update(arg.encode('utf-8'))
        result = str.hexdigest()
    return result



class Login:

    def __init__(self) -> None:
        self.db = DB(_host, _dbname, _username, _password)
        self.db.toConnect()
        self.result = []
        print("Teste")
    
    def login(email, passoword):
        print(email, passoword)