# This is Thread pool implemented as singleton

import threading
import time

from iWorkQ import *
from Light import *
from LightOnCmd import *
from Work import *
from iWorkerThread import *
from Singleton import *
	
class iWMS :
    # should be singleton
    def __init__(self) :
        pass;
        
    def init(self, wq, eList) :
        self.wq = wq
        self.eList = eList
        self.WAITING = 0
        self.RUNNING = 1


    def register(self, e) :
        for th in self.eList :
            if th.getName().lower() == e.getName.lower() :
                print "Already exist!"

                return Flase

        self.eList.append(e)
        print "registed successfully!"

        return True

    def delete(self, str) :
        for th in self.eList :
            if th.getName().lower() == str :
                self.eList.pop(th)
                print "deleted successfully!"
                return True

        print "Invalid name!"
        return False

    def findByName(self, str) :
        for th in self.eList :
            if th.getName().lower() == str :
                print "find successfully!"
                return th

    def retrieveAll(self) :
        print " :: There are %s Worker threads" % self.eList.size()
        
        for th in self.eList :
            print th.getName()

    def modify(self, oldStr, newStr) :
        for th in self.eList :
            if th.getName().lower() == oldStr :
                th.setName(newStr)
                print "Modified successfully!"

                return True

        print "Invalid name!"
        return False
           
    def isAvailableWorker(self) :
        for th in self.eList :
            if th.getStatus() == self.WAITING :
                return True

        return False

    def getAvailableWorker(self) :
        for th in self.eList :
            if th.getStatus() == self.WAITING :
                return th

        return ''

    def execute(self, r) :
        self.wq.enqueue(r)
        worker = self.getAvailableWorker()
        if worker != '' :
            worker.start()        
'''
class AAA(Singleton, iWMS) :
    pass
    
def test() :
    
    list = []
    wq = iWorkQ(list)
    
    light = Light()
    cmd = LightOnCmd(light)
    work = Work(cmd)

    worker = iWorkerThread('test', wq)

    thList = []
    #wms = iWMS(wq, thList)
    wms = AAA()
    wms.init(wq, thList)
    wms.register(worker)

    wms.execute(work)

test()
'''
