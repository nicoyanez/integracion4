from PyQt4.QtGui import QGraphicsPixmapItem ,QPixmap ,QAction ,QMenu
import random

class auto(QGraphicsPixmapItem):
      def __init__(self, *args):
            QGraphicsPixmapItem.__init__(self, *args)
            self.setPixmap(QPixmap("sprites/"+str(random.randint(1,45))+".png"))

            self.menu = QMenu()
            self.Actions =[] #arreglo de acciones 
            self.Actions.append( self.menu.addAction("Seguir") )
            self.Actions.append( self.menu.addAction("Editar") )
            self.Actions.append( self.menu.addAction("Mover") )
            self.Actions.append( self.menu.addAction("Eliminar") )
            self.menu.triggered[QAction].connect(self.test)
      def test(self,act):
            print act.text()
      def contextMenuEvent(self,event):
            self.menu.popup(event.screenPos())
      def mousePressEvent(self, event):
            print event
      def mouseMoveEvent(self, event):
            self.setPos(event.scenePos())

