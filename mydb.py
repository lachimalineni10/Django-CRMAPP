# Install MySQL
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Lachi_1305'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmapp")

print("All Done!")