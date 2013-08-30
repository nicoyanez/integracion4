from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QPushButton , QIcon
from auto import *
from calle2 import *
from bandejon2 import *
from centro2 import *

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

            ##
            self.auto1 = auto()
            self.auto1.setPos(100.0,150.0)
            self.auto1.setRotation(45)
            self.scene.addItem(self.auto1)
            

            ##calle
            c1 = calle()
            c1.setPos(200,200)
            self.scene.addItem(c1)

            ##central
            q1 = centro()
            q1.setPos(100,200)
            self.scene.addItem(q1)

            ##bandejon
            b1 = bandejon()
            b1.setPos(200,300)
            self.scene.addItem(b1)
            
            ##toolbar
            self.tb = QtGui.QToolBar("mi br",self)
            self.tb.setFixedSize(self.rect().width(),40)
            self.play = QPushButton(QIcon("icons/play.png"),"")
            self.tb.addWidget(self.play)

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
                  
