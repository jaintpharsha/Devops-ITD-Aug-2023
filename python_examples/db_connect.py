import mysql.connector
from mysql.connector import errorcode, MySQLConnection

try:
    db_connection = MySQLConnection(user='root', password='1234', port='3306', database='mydb')
    print("Database connection made!")
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is wrong")
    else:
        print(error)

cursor = db_connection.cursor()
sql = ("commands")
cursor.execute(sql)