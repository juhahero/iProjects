#import sys
#sys.path.append("D:\projects\GitHub\iProjects\iDevice\WMS")
#sys.path.append("D:\projects\GitHub\iProjects\iDevice\Interface")
#sys.path.append("D:\projects\GitHub\iProjects\iDevice\Server")
#sys.path.append("D:\projects\GitHub\iProjects\iDevice\Light")

from WMS.iWorkQ import *
from Light.Light import *
from Light.LightOnCmd import *
from WMS.Work import *
from WMS.iWorkerThread import *
from WMS.iWMS import *
from WMS.iWMSInstance import *
from Server.iRequestHandler import *
	

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
