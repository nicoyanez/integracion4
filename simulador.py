# -*- coding: utf-8 -*-
"""
Created on Sat Dec 07 10:58:43 2013

@author: nnn
"""
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import SIGNAL ,QObject

import threading ,time ,  thread
import inspect

lock = threading.Lock()

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()

def avanza(escena):
    #lock.acquire()
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    print "Inside %s()" % caller
    print "Acquiring lock"
    with lock:
        print "with lock"
        objetos = escena.scene.items()
        autos   = [i.avanza(i.velocity) for i in objetos if i.__class__.__name__=="auto" ]
        """ calles   = [i for i in objetos if i.__class__.__name__=="calle" ]
        centros   = [i for i in objetos if i.__class__.__name__=="centro" ]
        bandejones   = [i for i in objetos if i.__class__.__name__=="bandejon" ]
        cpasos = [i for i in objetos if i.__class__.__name__=="cpaso" ]
        pares = [i for i in objetos if i.__class__.__name__=="pare" ]
        semafoross = [i for i in objetos if i.__class__.__name__=="semaforo" ] """
        
        time.sleep(0.05)
        #avanza autos
        """ for i in autos:
            i.avanza(i.velocity) """
        
        QtCore.QObject.emit(escena,SIGNAL("RDY"),"SIMULATION READY MY FRIEND")
        print "senal enviada"
    
def simula(escena):
    """try:
        thread.start_new_thread( avanza, (escena, ) )
    except:
        print "no pude crear el hilo compadre" 
    t = threading.Thread(target=avanza, args=(escena,))  
    t.start()"""
    Thread(avanza,escena)