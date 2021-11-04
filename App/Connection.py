
import mysql.connector
import asyncio

# host = "sql527.main-hosting.eu"
# dbname = "u831868453_Eva"
# username = "u831868453_Eva"
# password = "s7RSmeME#"

class DB():
    
    def __init__(self, host = "sql527.main-hosting.eu", dbname = "u831868453_Eva", username = "u831868453_Eva", password = "s7RSmeME#") -> None:
        self._host = host
        self._dbname = dbname
        self._username = username
        self._password = password
    

    # CONECTAR AO BANCO DE DADOS
    def toConnect(self) -> bool:
        result = False
        self.con = mysql.connector.connect(
            host = self._host,
            user = self._username,
            password = self._password,
            database= self._dbname
        )

        if self.con:
            self.cursor = self.con.cursor()
            result = True

        return result

    
    def disconnect(self) -> bool:
        result = False

        if self.con:
            self.con.close()
            result = True

        return result
        
    
    def execute1(self, query = ""):
        result = None

        if self.toConnect() and query != "":
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.disconnect()

        return result

    def execute2(self, query = ""):
        result = None
        
        if self.toConnect() and query != "":
            self.cursor.execute(query)
            self.con.commit()
            # result = self.cursor.fetchall()
            self.disconnect()

        return result

class User():

    def __init__(self, username = "", password = "") -> None:
        self.username = username
        self.password = password

    


    def login(self, username="", password=""):
        query = "SELECT * FROM usuario WHERE usuario = '" + username + "' AND senha  = '" + password + "'"
        print(query)

if __name__ == "__main__":
    c = DB()
    

    result = []

    query = "SELECT * FROM usuario"
    result = c.execute1(query)

    if result != None: 
        for a in result:
            print(a[1])


    print("TESTE")







# conn = mysql.connector.connect(host = host, user = username, password = password, database= dbname)
#  # cursor.execute("SELECT * FROM usuario")
    
#     # result = cursor.fetchall()

#     # for a in result:
#     #     print(a[1])

#     # result = JSON

# if conn:
#     db_info = conn.get_server_info()
#     print("# Conexão realizada com sucesso!\nVersão do MySql: ", db_info)





# def login(username = "", password = ""):
#     cursor = conn.cursor()
#     query = "SELECT * FROM usuario WHERE usuario = '" + username + "' AND senha  = '" + password + "'"
#     cursor.execute(query)
#     result = cursor.fetchone()

#     if result:
#         print("# SUCCESS!")
#         print(result)
#     else:
#         print("[!] ERRO!")



# if __name__ == "__main__":
#     user = "Eva"
#     senha = "202cb962ac59075b964b07152d234b70"
#     login("Eva", "202cb962ac59075b964b07152d234b70")



