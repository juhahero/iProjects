# This is LightCmd implemented Command

from Light import *
from ..Interface.Command import *

class LightOnCmd(Command) :

    def __init__(self, obj) :
        self.obj = obj

    def execute(self) :
        self.obj.On()
        
'''
def test() :
    light = Light()
    lightOn = LightOnCmd(light)
    lightOn.execute()

test()
'''
