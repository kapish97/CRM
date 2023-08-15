import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin'
)

# cursor object
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE kapishdb")

print('DONE')