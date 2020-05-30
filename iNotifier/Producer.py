import threading
import random
import time


class Producer(threading.Thread) :
    def __init__(self, queue, crawl) :
        threading.Thread.__init__(self)
        self.pool = queue
        self.crawler = crawl
        
    def run(self) :
        while(True) :
            #obj = random.randint(0, 256)
            obj = self.crawler.crawledData()
            print ("Producer : enqueue obj = %s\n" %obj)
            self.pool.enqueue(obj)                
            
            time.sleep(10)
