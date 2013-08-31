from PyQt4.QtGui import QGraphicsPixmapItem ,QPixmap ,QAction ,QMenu
from PyQt4.QtCore import QPointF
from abstractPixmapScene import *
class pare(abstractPixmapScene):
      def __init__(self, *args):
            abstractPixmapScene.__init__(self, img=QPixmap("sprites/calle/pare.png"))
            self.setTransformOriginPoint(self.boundingRect().width()/2,self.boundingRect().height())
            self.setZValue(11)
      def duplicame(self):
            self.scene().addItem(pare())
