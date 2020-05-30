import threading
import random
import time
from iWorker import *

class Consumer(threading.Thread) :
    def __init__(self, queue, worker) :
        threading.Thread.__init__(self)
        self.pool = queue
        self.worker = worker
        

    def run(self) :
        while(True) :
            job = self.pool.dequeue()
            print ("Consumer : dequeue job = %s\n" %job)
            self.worker.runJob(job)
            #self.worker.start()
            time.sleep(1)
