# -*- coding: utf-8 -*-
"""
Created on Sun Dec 08 13:16:38 2013

@author: nnn
"""
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL ,QObject , QThread 
import time,random
global mutex
mutex = QtCore.QMutex()
hilos = []
class simulador(QtCore.QThread):
    def __init__(self,escena):
        super(simulador , self).__init__()
        self.escena = escena
        #self.mutex = QtCore.QMutex()
        self.start()
    def run(self):
        while 1:
            temp = ""
            time.sleep(0.1)
            mutex.lock()
            objetos = self.escena.scene.items()
            #autos   = [i.avanza() for i in objetos if i.__class__.__name__=="auto" ]
            for i in objetos:
                if i.__class__.__name__=="auto":
                    i.avanza()
                    #i.setRotation(i.rotation() + random.randint(-10,10))
                    if i.seleccionado:
                        temp+=i.info()
                    """for j in i.collidingItems():
                        if i.velocity !=0 and ( j.__class__.__name__=="auto" or  j.__class__.__name__=="bandejon" ):
                            i.velocity = 0
                            j.velocity=0 """
            mutex.unlock()
            QtCore.QObject.emit(self.escena,SIGNAL("RDY"),("SIMULATION READY MY FRIEND\n"+temp))
            print "senal enviada"
        self.terminate()
def simula(escena):
    hilos.append( simulador(escena) )