class Singleton(object) :
    
    _instance = None
    
    def __new__(cls, *args, **kwargs) :
        if not cls._instance :
            cls._instance = object.__new__(cls, *args, **kwargs)
            
        return cls._instance      
    '''
    _instances = {}
    def __call__(cls, *args, **kwargs) :
        if cls not in cls._instances :
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    '''

'''
#TEST##############################
class BaseClass :    
    #__metaclass__ = Singleton
    #var = 0
    def __init__(self) :
        pass
        #self.var = 0

    def init(self, i) :
        self.var = i
        
    def getStatus(self) :
        return self.var
        
    def setStatus(self, i) :
        self.var = self.var + i

class AAA(Singleton, BaseClass) :
    #__metaclass__ = Singleton    
    pass

a1 = AAA()
a1.init(100)

a1.setStatus(5)
print 'a1 = %d' % a1.getStatus()
a2 = AAA()
a2.setStatus(20)

print a2.getStatus()
print a1.getStatus()
'''        
