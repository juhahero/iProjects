# This is workqueue(FIFO)
# using Producer/Consumer pattern
import threading

class iWorkQ :
    
    pool = ''
    POOL_MAX = 10
    
    def __init__(self, LinkedList) :
        pool = LinkedList
        self.mutex = thread.Lock()
        self.condition = threading.Condition(self.mutex)
    
    def enqueue(self, obj) :
        global POOL_MAX
        global pool
        
        while (self.size() >= POOL_MAX) :
            try :
                print "wait enqueue...."
                self.condition.wait()
            except InterruptedException, msg:
                print 'InterruptedException : ', msg
            else :
                pass
        
        
        pool.append(obj)
        
        if (self.size() > 0) :
            print "notify enqueue...."
            self.condition.notifyAll()
    
    def dequeue(self) :
        global POOL_MAX
        global pool
        
        while (self.size() == 0) :
            try :
                print "wait dequeue...."
                self.condition.wait()
            except InterruptedException, msg :
                
                print 'InterruptedException : ', msg
            else :
                pass
        
        obj = pool.pop(0)
        if (self.size() < POOL_MAX) :
            print "notify dequeue...."
            self.condition.notifyAll()
        
        return obj
    
    def size(self) :
        return pool.count()
    
    def isEmpty(self) :
        if (self.size() == 0) :
            return True
        
        return False

