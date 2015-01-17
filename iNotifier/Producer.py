import threading
import random
import time

class Producer(threading.Thread) :
    def __init__(self, queue) :
        threading.Thread.__init__(self)
        self.pool = queue

    def run(self) :
        while(True) :
            for i in range(5) :
                obj = random.randint(0, 256)
                print "Producer : enqueue obj = %d\n" %obj
                self.pool.enqueue(obj)                
            
            time.sleep(1)
