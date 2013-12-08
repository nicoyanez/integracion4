from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QPushButton , QIcon , QComboBox , QLabel , QDialog , QVBoxLayout ,QLineEdit
from PyQt4.QtCore import QStringList , QString
import sqlite3
from auto import *
from calle import *
from bandejon import *
from centro import *
from semaforo import *
from cpaso import *
from pare import *
from sys import *
from simulador2 import *

objetos = {"auto":auto,"bandejon":bandejon,"calle":calle,"centro":centro,"cpaso":cpaso,"semaforo":semaforo,"pare":pare}

class escena(QtGui.QWidget):
      def __init__(self, *args):
            QtGui.QWidget.__init__(self, *args)
            self.layout = QtGui.QVBoxLayout()
            self.setLayout(self.layout)
            self.resize(900, 600)
            self.setAcceptDrops(True)


            ##escena
            self.scene = QtGui.QGraphicsScene(0,0,self.rect().width(),self.rect().height())
            self.view = QtGui.QGraphicsView(self)
            self.view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.view.setAcceptDrops(True)
            self.view.dragMoveEvent = self.dragMoveEvent
            self.view.dropEvent = self.dropEvent
            self.view.wheelEvent = self.viewWeelEvent
            self.view.dragEnterEvent = self.dragEnterEvent            
            self.view.setScene(self.scene)
            self.view.setGeometry(QtCore.QRect(0, 0, self.rect().width()-100, self.rect().height()-40))

            ##escenario por defecto 
            ##autos
            
            self.auto1 = auto()
            self.auto1.setPos(200.0,150.0)
            self.auto1.setRotation(45)
            self.scene.addItem(self.auto1)

            self.auto2 = auto()
            self.auto2.setPos(100.0,150.0)
            self.auto2.setRotation(90)
            self.scene.addItem(self.auto2)

            self.auto3 = auto()
            self.auto3.setPos(100.0,150.0)
            self.auto3.setRotation(90)
            self.scene.addItem(self.auto3)

            
            self.auto4 = auto()
            self.auto4.setPos(200.0,420.0)
            self.auto4.setRotation(120)
            self.scene.addItem(self.auto4)

            self.auto5 = auto()
            self.auto5.setPos(1250.0,100.0)
            self.auto5.setRotation(90)
            self.scene.addItem(self.auto5)

            self.auto6 = auto()
            self.auto6.setPos(400.0,250.0)
            self.auto6.setRotation(0)
            self.scene.addItem(self.auto6)

            self.auto7 = auto()
            self.auto7.setPos(1250.0,500.0)
            self.auto7.setRotation(90)
            self.scene.addItem(self.auto7)
            ##calle
            x=0
            y=30
            c1=[calle() for i in range(0,3)]
            for j in c1:
                  
                  j.setPos(x,y)
                  j.setRotation(90)
                  self.scene.addItem(j)
                  y=y+200
            x=140
            y=30
            c2=[calle() for i in range(0,3)]
            for j in c2:
                  
                  j.setPos(x,y)
                  j.setRotation(270)
                  self.scene.addItem(j)
                  y=y+200
            x=1070
            y=30
            c3=[calle() for i in range(0,3)]
            for j in c3:
                  
                  j.setPos(x,y)
                  j.setRotation(90)
                  self.scene.addItem(j)
                  y=y+200
            x=1210
            y=30
            c4=[calle() for i in range(0,3)]
            for j in c4:
                  
                  j.setPos(x,y)
                  j.setRotation(270)
                  self.scene.addItem(j)
                  y=y+200
            ##central
            q= [centro() for i in range(0,4)]      
            x = 305
            y = 240
            for i in q:
                  
                  i.setPos(x,y)
                  self.scene.addItem(i)
                  x=x+200
            
            ##bandejon
            b=[bandejon() for i in range(0,4)]
            x=310
            y=0
            for i in b:
                  i.setPos(x,y)
                  x=x+198
                  self.scene.addItem(i)
            b2=[bandejon() for i in range(0,4)]
            x=310
            y=120
            for i in b2:
                  i.setPos(x,y)
                  x=x+198
                  self.scene.addItem(i)
            
            b3=[bandejon() for i in range(0,4)]
            x=310
            y=400
            for i in b3:
                  i.setPos(x,y)
                  x=x+198
                  self.scene.addItem(i)
            b4=[bandejon() for i in range(0,4)]
            x=310
            y=500
            for i in b4:
                  i.setPos(x,y)
                  x=x+198
                  self.scene.addItem(i)
            
            ##semaforo
            s1 = semaforo()
            s1.setPos(200,200)
            self.scene.addItem(s1)

            ##pare
            p1= pare()
            self.scene.addItem(p1)
            ##ceda el paso 
            cp1 = cpaso()
            self.scene.addItem(cp1)
            
            ##toolbar
            self.tb = QtGui.QToolBar("mi br",self)
            self.tb.setFixedSize(self.rect().width(),40)
            #boton play
            self.play = QPushButton(QIcon("icons/play.png"),"")
            self.tb.addWidget(self.play)
            self.play.clicked.connect(self.iniciaSimulacion)
            #boton pausa
            self.pausa = QPushButton(QIcon("icons/pause.png"),"")
            self.tb.addWidget(self.pausa)
            self.pausa.clicked.connect(self.pausaSimulacion)
            ##combo de escenarios predefinidos
            self.tb.addSeparator()
            self.tb.addWidget(QLabel("Cargar escenario"))
            self.combo = QComboBox()
            tablas = self.cargaTablas()
            self.combo.addItems(tablas)
            #combo = QComboBox()
            #combo.addItems(["Scene #1","Scene #2","Scene #3"])
            self.combo.currentIndexChanged[QString].connect(self.cambiaEscenario)
            self.tb.addWidget(self.combo)
            ##boton de guardar escenario
            self.tb.addSeparator()
            bge = QPushButton("Guardar")
            self.tb.addWidget(bge)
            bge.clicked.connect(self.guardaEscenario)
            acepta = QPushButton("Aceptar")
            acepta.clicked.connect(self.aceptar)
            self.dialogo = QDialog()
            layout = QVBoxLayout()
            self.name = QLineEdit("Mi Escenario #1")
            layout.addWidget(self.name)
            layout.addWidget(acepta)
            self.dialogo.setLayout(layout)
            QtCore.QObject.connect(self, QtCore.SIGNAL('RDY'), self.repinta)
            self.simulando = False
            self.simulaciones = []
      def repinta(self,arg):
          print "repintado"
          if self.simulando:
              self.scene.update()
              self.repaint()
              self.simulaciones.append( simula(self) )
              
      def iniciaSimulacion(self):
          print "iniciaodo simulacion"
          self.simulando = True
          simula(self)
      def pausaSimulacion(self):
          print "pausa simulacion"
          self.simulando = False
      def cargaTablas(self):
            temp = QStringList("Elija Una Fuente")
            connection = None
            try:
                  connection =  sqlite3.connect("escenarios.db")
                  cursor = connection.cursor()
                  cursor.execute("SELECT name FROM escenario")
                  data = cursor.fetchall()
                  for row in data:
                        temp.append(row[0])
                        #print row[0]
            except sqlite3.Error , e:
                  print "Error %s:" % e.args[0]
                  if connection:
                        connection.close()
            return temp
      def aceptar(self):
            self.dialogo.accept()
      def guardaEscenario(self):
            connection = None
            id_escenario = 0
            if self.dialogo.exec_():
                  try:
                      connection =  sqlite3.connect("escenarios.db")
                      cursor = connection.cursor()
                      cursor.execute("insert into escenario (name) values (?)",[str(self.name.text())])
                      connection.commit()
                      id_escenario = cursor.lastrowid
                      for item in self.scene.items():
                            if item.__class__.__name__!="QGraphicsPolygonItem":
                                  #print item.__class__.__name__
                                  #item.__class__.__name__,item.pos().x(),":",item.pos().y(),":",item.rotation()
                                  cursor.execute("insert into posiciones (escenario_id,objeto_id,x,y,angle) values (?,(select id from objetos where name=? ),?,?,?) ",[id_escenario,item.__class__.__name__,item.pos().x(),item.pos().y(),item.rotation()])
                      connection.commit()
                      id_escenario = cursor.lastrowid
                  except sqlite3.Error , e:
                      print "Error %s:" % e.args[0]
                  if connection:
                      connection.close()
                  print "se guardaran los cambios"
                  tablas = self.cargaTablas()
                  self.combo.clear()
                  self.combo.addItems(tablas)
                  self.combo.setCurrentIndex(len(tablas)-1)
                  print "se actualizo el combo"
            else:
                  print "no se guarda nada"
      def cambiaEscenario(self,name):
            self.scene.clear()
            print "se carga el escenario",name
            try:
                  connection =  sqlite3.connect("escenarios.db")
                  cursor = connection.cursor()
                  cursor.execute("select objetos.name,posiciones.x,posiciones.y,posiciones.angle from posiciones inner join objetos on objetos.id = posiciones.objeto_id where escenario_id = (select id from escenario where name= ?)",[str(name)])
                  #connection.commit()
                  data = cursor.fetchall()
                  for row in data:
                        #print row
                        temp = objetos[row[0]]()
                        temp.setPos(row[1],row[2])
                        temp.setRotation(row[3])
                        self.scene.addItem(temp)
                  self.scene.update()
            except sqlite3.Error , e:
                  print "Error %s:" % e.args[0]
            if connection:
                  connection.close()
      def viewWeelEvent(self,event):
            None
      def imprime(self,event):
            print event
      def resizeEvent(self,event):
            #print self.rect()
            self.tb.setFixedSize(self.rect().width(),40)
            self.scene.setSceneRect(0,0,self.rect().width(),self.rect().height()-40)
            #self.view.setSceneRect(0,0,self.rect().width(),self.rect().height())
            self.view.setGeometry(QtCore.QRect(0, 40, self.rect().width(), self.rect().height()-40))
      def dragMoveEvent(self,e):
            #print e
            None
      def dragEnterEvent(self, e):
            e.accept()
            #print e
            """if e.mimeData().hasFormat('text/plain'):
                  e.accept()
            else:
                  e.ignore()"""
      def dropEvent(self, e):
            print e.mimeData().text()
            self.repaint()
      def paintEvent(self,event):
          qp = QtGui.QPainter()
          qp.begin(self)
          self.draw(event,qp)
          qp.end()
      
      def draw(self,event,qp):
          pen = QtGui.QPen(QtGui.QColor(255, 0, 0), 5, QtCore.Qt.SolidLine)
          qp.setPen(pen)
          #self.scene.update(0,0,self.rect().width(),self.rect().height())
      def keyPressEvent(self,event):
            k = event.key()
            #print "la tecla es ",k
            if k == 65:
                  self.auto1.setRotation(self.auto1.rotation()-5)
            if k == 68:
                  self.auto1.setRotation(self.auto1.rotation()+5)
                  

    
