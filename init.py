from escena import *

from PyQt4 import QtCore
from PyQt4 import QtGui
import sys


class MainWindow(QtGui.QMainWindow):
      def __init__(self, parent=None):
            QtGui.QMainWindow.__init__(self, parent)
            self.setWindowTitle('Mi ventana')
            self.resize(900, 600)
            self.statusBar().showMessage("Listo")
            self.contenedir = QtGui.QVBoxLayout()
            self.w = escena()
            self.setCentralWidget(self.w)
      def closeEvent(self, event):
            print "chao"
if __name__ == "__main__":
      app = QtGui.QApplication(sys.argv)
      #w = MyWindow()
      w = MainWindow()
      w.show()
      print app.exec_()
