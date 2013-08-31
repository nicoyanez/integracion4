from PyQt4.QtGui import QGraphicsPixmapItem ,QPixmap ,QAction ,QMenu ,QGraphicsPolygonItem , QPolygonF  , QColor
from PyQt4.QtCore import QPointF
import random

class auto(QGraphicsPixmapItem):
      def __init__(self, *args):
            QGraphicsPixmapItem.__init__(self, *args)
            self.setPixmap(QPixmap("sprites/"+str(random.randint(1,45))+".png"))
            self.setTransformOriginPoint(self.boundingRect().width()/2.0,self.boundingRect().height()/2.0)
            self.setZValue(10)
            ##menu contextual
            self.menu = QMenu()
            self.Actions =[] #arreglo de acciones 
            self.Actions.append( self.menu.addAction("Seguir") )
            self.Actions.append( self.menu.addAction("Editar") )
            self.Actions.append( self.menu.addAction("girar clockwise") )
            self.Actions.append( self.menu.addAction("girar anti-clockwise") )
            self.Actions.append( self.menu.addAction("Colisiones") )
            self.Actions.append( self.menu.addAction("Duplicar") )
            self.Actions.append( self.menu.addAction("Eliminar") )
            self.menu.triggered[QAction].connect(self.test)
            ##offset para el arrastre
            self.offset= QPointF(0,0)
            ##poligono de vision
            poligono = QPolygonF()
            poligono.append(QPointF(-1,10))
            poligono.append(QPointF(-1,20))
            poligono.append(QPointF(-30,40))
            poligono.append(QPointF(-40,15))
            poligono.append(QPointF(-30,-10))
            self.vision = QGraphicsPolygonItem(poligono,self,self.scene())
            self.vision.setBrush(QColor(255, 255, 0,100))
            self.vision.setPen(QColor(255, 255, 0))

      def test(self,act):
            print act.text()
            if act.text()=="girar clockwise":
                  self.setRotation(self.rotation()-45)
            if act.text()=="girar anti-clockwise":
                  self.setRotation(self.rotation()+45)
            if act.text()=="Colisiones":
                  print "colisiones con",self.collidingItems(1),self.vision.collidingItems(1)
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

