# This is Work class for job
# Worker handles command capsuled using command pattern

import threading
import time
from Light import *
from LightOnCmd import *


class Work(threading.Thread) :
    def __init__(self, cmd) :
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self) :
        self.cmd.execute()
        time.sleep(1)

'''    
def test() :
    light = Light()
    cmd = LightOnCmd(light)
    work = Work(cmd)
    work.start()

test()
'''
