import mysql.connector as mysql


class DB():
    
    def __init__(self, host = '', dbname = '', username = '', password = "") -> None:
        self._host = host
        self._dbname = dbname
        self._username = username
        self._password = password

    # CONECTAR AO BANCO DE DADOS
    def toConnect(self) -> bool:
        result = None
        try:
            self.conn = mysql.connect(
                host = self._host,
                db =  self._dbname,
                user = self._username,
                passwd = self._password
            )

            if self.conn.is_connected():
                print("# CONEXÃO REALIZADA COM SUCESSO!")
                result = True
            else:
                print('[!] ERRO AO CONECTAR COM O BANCO DE DADOS')
                result = False
        except:
            print("[!] ERRO AO SE COMUNICAR COM DB")
            result = False
        
        return result
    
    def disconnect(self) -> bool:
        result = None

        try:
            if self.conn:
                self.conn.close()
                result = True
        except:
            result = False

        return result
    
    def commit(self):
        try:
            self.conn.commit()
        except:
            print("[!] COMMIT")

    def cursor(self, query = "", tupla = ()):
        result = None

        try:
            
            if self.conn and query != "":
                cursor = self.conn.cursor()
                self.result = cursor.execute(query, tupla)
                result = True

        except:
            result = False

        return result

    def fetchAll(self, query = "", tupla = ()):
        result = None

        try:
            if self.conn and query != "":
                cursor = self.conn.cursor()
                cursor.execute(query, tupla)
                result = cursor.fetchall()

        except:
            result = False

        return result

    def fetchOne(self, query = "",  tupla = ()):
        result = None

        # query = 'SELECT * FROM users_class'

        
        try:
            if self.conn and query != "":
                cursor = self.conn.cursor()
                cursor.execute(query, tupla)
                result = cursor.fetchone()

        except:
            result = False

        return result