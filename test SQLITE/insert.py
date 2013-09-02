import sqlite3

connection = None
try:
    connection =  sqlite3.connect("escenarios.db")
    cursor = connection.cursor()
    cursor.execute("drop table IF EXISTS escenario")
    cursor.execute("create table escenario (ID INTEGER PRIMARY KEY   AUTOINCREMENT, name TEXT)")
    cursor.execute("drop table IF EXISTS objetos")
    cursor.execute("create table objetos(ID INTEGER PRIMARY KEY   AUTOINCREMENT, name TEXT)")
    cursor.execute("drop table IF EXISTS posiciones")
    cursor.execute("create table posiciones \
                   (escenario_id integer, \
                    objeto_id integer,\
                    x real,y real,angle real, \
                    foreign key(escenario_id) references escenario(id),\
                    foreign key(objeto_id) references objetos(id))")
    cursor.execute("insert into escenario values (0,?)",["Escenario uno"])
    cursor.execute("insert into escenario(name) values (?)",["Escenario dos"])
    cursor.execute("insert into escenario(name) values (?)",["Escenario tres"])
    cursor.execute("insert into objetos(name) values (?)",["auto"])
    cursor.execute("insert into objetos(name) values (?)",["bandejon"])
    cursor.execute("insert into objetos(name) values (?)",["calle"])
    cursor.execute("insert into objetos(name) values (?)",["centro"])
    cursor.execute("insert into objetos(name) values (?)",["cpaso"])
    cursor.execute("insert into objetos(name) values (?)",["pare"])
    cursor.execute("insert into objetos(name) values (?)",["semaforo"])
    
    connection.commit()
except sqlite3.Error , e:
    print "Error %s:" % e.args[0]
if connection:
    connection.close()
print "termino todo"
