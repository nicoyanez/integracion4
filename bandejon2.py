from PyQt4.QtGui import QGraphicsPixmapItem ,QPixmap ,QAction ,QMenu
from PyQt4.QtCore import QPointF
from abstractPixmapScene import *
class bandejon(abstractPixmapScene):
      def __init__(self, *args):
            abstractPixmapScene.__init__(self, img=QPixmap("sprites/calle/bandejon.png"))
      def duplicame(self):
            self.scene().addItem(bandejon())
