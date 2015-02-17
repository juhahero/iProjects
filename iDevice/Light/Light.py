# This is Recevier for Command pattern

from iControl import *
import time

class Light :

    def __init__(self, control) :
        self.ON = '1'
        self.OFF = '0'
        self.control = control

    def On(self) :
        print 'Light:On() = %s' % self.ON
        self.control.setOnOff(self.ON)

    def Off(self) :
        print 'Light:Off() = %s' % self.OFF
        self.control.setOnOff(self.OFF)

def test() :
    ser = serial.Serial("COM6", 9600)
    ictrl = iControl(ser)
    light = Light(ictrl)
    light.On()

#test()
