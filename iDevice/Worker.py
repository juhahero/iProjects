# This is Work class for job
# Worker handles command capsuled using command pattern

import threading
from LightOnCmd import *

class Worker(threading.Thread) :
    def __init__(self, cmd) :
        self.cmd = cmd

    def run(self) :
        self.cmd.execute()
        

'''    
def test() :
    LightOnCmd cmd = new LightOnCmd()
    Worker work = new Worker(cmd)
    work.start()
'''
    
