from PyQt4.QtGui import QGraphicsPixmapItem ,QPixmap ,QAction ,QMenu
from PyQt4.QtCore import QPointF
import random

class auto(QGraphicsPixmapItem):
      def __init__(self, *args):
            QGraphicsPixmapItem.__init__(self, *args)
            self.setPixmap(QPixmap("sprites/"+str(random.randint(1,45))+".png"))
            self.setTransformOriginPoint(self.boundingRect().width()/2.0,self.boundingRect().height()/2.0)
            self.setZValue(10)
            self.menu = QMenu()
            self.Actions =[] #arreglo de acciones 
            self.Actions.append( self.menu.addAction("Seguir") )
            self.Actions.append( self.menu.addAction("Editar") )
            self.Actions.append( self.menu.addAction("Colisiones") )
            self.Actions.append( self.menu.addAction("Duplicar") )
            self.Actions.append( self.menu.addAction("Eliminar") )
            self.menu.triggered[QAction].connect(self.test)
            self.offset= QPointF(0,0)
      def test(self,act):
            print act.text()
            if act.text()=="Colisiones":
                  print "colisiones con",self.collidingItems(1)
            if act.text()=="Duplicar":
                  self.scene().addItem(auto())
            if act.text()=="Eliminar":
                  self.scene().removeItem(self)
      def contextMenuEvent(self,event):
            self.menu.popup(event.screenPos())
      def mousePressEvent(self, event):
            p = event.pos()
            self.offset= QPointF(p.x()*1.0,p.y()*1.0)
      def mouseMoveEvent(self, event):
            self.setPos(event.scenePos()-self.offset)

