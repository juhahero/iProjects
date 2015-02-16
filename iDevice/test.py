from iWorkQ import *
from Light import *
from LightOnCmd import *
from Work import *
from iWorkerThread import *
from iWMS import *
from iWMSInstance import *
from iRequestHandler import *
	

def init_WMS()  :   
    list = []
    wq = iWorkQ(list)

    worker = iWorkerThread('test', wq)

    thList = []
    wms = iWMSInstance()
    wms.init(wq, thList)
    wms.register(worker)

    #wms.execute(work)

def serverRun() :
    SOCKTest()
    
init_WMS()
serverRun()
