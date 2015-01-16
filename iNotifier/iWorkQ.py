# This is workqueue
# using Producer/Consumer pattern

class WorkQueue :
    
    pool = ''
    POOL_MAX = 10
    
    def __WorkQ__(self, LinkedList) :
        pool = LinkedList 
    
    def enqueue(self, obj) :
        global POOL_MAX
        global pool
        
        while (self.size() >= POOL_MAX) :
            try :
                print "wait enqueue...."
                wait()
            except InterruptedException, msg:
                print 'InterruptedException : ', msg
            else :
                pass
        
        
        pool.add(obj)
        
        if (size() > 0) :
            print "notify enqueue...."
            notifyAll()
    
    def dequeue(self) :
        global POOL_MAX
        global pool
        
        while (self.size() == 0) :
            try :
                print "wait dequeue...."
                wait()
            except InterruptedException, msg :
                
                print 'InterruptedException : ', msg
            else :
                pass
        
        obj = pool.removeFirst()
        if (self.size() < POOL_MAX) :
            System.out.println("notify dequeue....")
            notifyAll()
        
        return obj
    
    def size(self) :
        return pool.size()
    
    def isEmpty(self) :
        if (self.size() == 0) :
            return True
        
        return False

