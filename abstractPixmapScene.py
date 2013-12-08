from PyQt4.QtGui import QGraphicsPixmapItem ,QPixmap ,QAction ,QMenu
from PyQt4.QtCore import QPointF
class abstractPixmapScene(QGraphicsPixmapItem):
      def __init__(self, img):
            QGraphicsPixmapItem.__init__(self)
            self.setPixmap(img)
            self.setTransformOriginPoint(self.boundingRect().width()/2.0,self.boundingRect().height()/2.0)
            self.setZValue(1)
            self.menu = QMenu()
            self.Actions =[] #arreglo de acciones 
            self.Actions.append( self.menu.addAction("girar clockwise") )
            self.Actions.append( self.menu.addAction("girar anti-clockwise") )
            self.Actions.append( self.menu.addAction("Duplicar") )
            self.Actions.append( self.menu.addAction("Eliminar") )
            self.menu.triggered[QAction].connect(self.test)
            self.offset=QPointF(0,0)
      def test(self,act):
            print act.text()
            if act.text()=="girar clockwise":
                  self.setRotation(self.rotation()-45)
            if act.text()=="girar anti-clockwise":
                  self.setRotation(self.rotation()+45)
            if act.text()=="Duplicar":
                  #self.scene().addItem(bandejon())
                  self.duplicame()
            if act.text()=="Eliminar":
                  self.scene().removeItem(self)
      def contextMenuEvent(self,event):
            self.menu.popup(event.screenPos())
      def mousePressEvent(self, event):
            p = event.pos()
            self.offset= QPointF(p.x()*1.0,p.y()*1.0)
      def mouseMoveEvent(self, event):
            self.setPos(event.scenePos()-self.offset)
            self.scene().update()
      def duplicame(self):
            print "duplicando"

