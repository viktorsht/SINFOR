from App.Db import DB

try:
    from App.credentials import _host, _dbname, _username, _password
except:
    print("[!]  ARQUIVO CREDENCIAIS!")
    exit()




if __name__ == "__main__":
    
    db = DB(_host, _dbname, _username, _password)
    db.toConnect()