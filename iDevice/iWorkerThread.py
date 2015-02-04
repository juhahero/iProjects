# This is worker thread for handling job dequeued from workqueue

import threading
import time

from iWorkQ import *
from Light import *
from LightOnCmd import *
from Work import *

class iWorkerThread(threading.Thread) :
    def __init__(self, name, wq) :
        threading.Thread.__init__(self)
        self.WAITING = 0
        self.RUNNING = 1

        self.name = name
        self.work = ''
        self.status = self.WAITING

        #self.wq = WorkQueue.getInstance()
        self.wq = wq
        
    def getName(self) :
        return self.name

    def getStatus(self) :
        return self.status

    def setStatus(self, st) :
        self.status = st

    def setWork(self, job) :
        self.work = job

    def run(self) :
        while True :
            job = self.wq.dequeue()
            self.setWork(job)
            self.setStatus(self.RUNNING)

            #job.run() # should be runnable
            job.start()

            if self.wq.size() <= 0 :
                break

        self.setStatus(self.WAITING)

'''        
def test() :
    list = []
    wq = iWorkQ(list)
    
    light = Light()
    cmd = LightOnCmd(light)
    work = Work(cmd)

    wq.enqueue(work)
    time.sleep(1)

    worker = iWorkerThread('test', wq)
    worker.start()

test()
'''
