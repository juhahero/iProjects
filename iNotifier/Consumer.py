import threading
import random
import time

class Consumer(threading.Thread) :
    def __init__(self, queue) :
        threading.Thread.__init__(self)
        self.pool = queue
        

    def run(self) :
        while(True) :
            job = self.pool.dequeue()
            print "Consumer : dequeue job = %s\n" %job
            time.sleep(1)
