import mysql.connector as mariadb
from Classes import *

db_user = "root"
db_password = "password"
db_name = "operationeventhub"

class Users():
    def __init__(self):
        self.mariadb_connection = mariadb.connect(user=db_user, password=db_password, database=db_name)
        self.cursor = self.mariadb_connection.cursor()
    
    def addUser(self,uid,username,password,email,phonenumber):
        self.cursor.execute("INSERT INTO users VALUES (%s,%s,%s,%s,%s)",(uid,username,password,email.phonenumber))
        self.mariadb_connection.commit()
        
    def getUser(self,username):
        self.cursor.execute("SELECT * FROM users WHERE username=%s",(username,))
        for uid,username,password,email,phonenumber in self.cursor:
            return User(uid,username,password,email,phonenumber)
    
    #TODO: impement proper error handling

class Posts():
    def __init__(self):
        pass

class Events():
    def __init__(self):
        pass

class Attractions():
    def __init__(self):
        pass
