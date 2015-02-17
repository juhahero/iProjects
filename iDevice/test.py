import sys
sys.path.append("D:\projects\GitHub\iProjects\iDevice\WMS")
sys.path.append("D:\projects\GitHub\iProjects\iDevice\Interface")
sys.path.append("D:\projects\GitHub\iProjects\iDevice\Server")
sys.path.append("D:\projects\GitHub\iProjects\iDevice\Light")

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
