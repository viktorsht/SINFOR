from App.Db import DB
from App.credentials import _host, _dbname, _username, _password



if __name__ == "__main__":

    print(_host, _dbname, _username, _password)
    
    db = DB(_host, _dbname, _username, _password)
    db.toConnect()