# This is workqueue(FIFO)
# using Producer/Consumer pattern
import threading
            
class iWorkQ :
    
    pool = ''
    POOL_MAX = 10
    
    def __init__(self, queue) :
        self.pool = queue
        self.mutex = threading.Lock()
        self.condition = threading.Condition(self.mutex)
    
    def enqueue(self, obj) :
        #global POOL_MAX
        #global pool

        self.condition.acquire()
        while (self.size() >= self.POOL_MAX) :
            print ('wait enqueue....\n')
            self.condition.wait()       
        
        self.pool.append(obj)
        
        if (self.size() > 0) :
            print ('notify enqueue....\n')
            self.condition.notifyAll()
        self.condition.release()
        
    def dequeue(self) :
        #global POOL_MAX
        #global pool

        self.condition.acquire()
        while (self.size() == 0) :
            print ('wait dequeue....\n')
            self.condition.wait()

        
        obj = self.pool.pop(0)
        if (self.size() < self.POOL_MAX) :
            print ('notify dequeue....\n')
            self.condition.notifyAll()
        self.condition.release()
        
        return obj
    
    def size(self) :
        return len(self.pool)
    
    def isEmpty(self) :
        if (self.size() == 0) :
            return True
        
        return False


