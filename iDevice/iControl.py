import serial
import time

class iControl :
    def __init__(self, ser) :
        self.ser = ser
        
    def setOnOff(self, cmd) :
        ser.write(cmd)
        
    def isAvailable(self, cmd) :
        ser.write(cmd)
        while True :
            if ser.readline() == 'available' :
                return True
            else 
                return False
                
    def getCurrentStatus(self) :
        ser.write(cmd)
        while True :
            if (result = ser.readline()) != ''
                print result
                return
                
    def readLine(self) : 
        return ser.readline()

'''         
def test() :
    ser = serial.Serial("COM1", 9600)
    ictrl = new iControl(ser)
    
    print ictrl.readLine()        

test()
'''