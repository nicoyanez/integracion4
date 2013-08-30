from PyQt4.QtGui import QGraphicsPixmapItem ,QPixmap ,QAction ,QMenu
from PyQt4.QtCore import QPointF
from abstractPixmapScene import *
import random
class auto(abstractPixmapScene):
      def __init__(self, *args):
            abstractPixmapScene.__init__(self, img=QPixmap("sprites/calle/"+str(random.randint(1,45))+".png"))

