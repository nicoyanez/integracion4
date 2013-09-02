import sqlite3
import sys

connection = None
try:
    connection =  sqlite3.connect("escenarios.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #cursor.execute("SELECT * FROM prueba1;")
    data = cursor.fetchall()
    for row in data:
        r= str(row[0])
        if not ("sqlite_" in r):
            print row[0]
except sqlite3.Error , e:
    print "Error %s:" % e.args[0]
if connection:
    connection.close()
    print "\nse cerro la conexion"
print "termino todo"
