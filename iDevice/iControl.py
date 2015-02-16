import serial
import time

class iControl :
    def __init__(self, ser) :
        self.ser = ser
        
    def setOnOff(self, cmd) :
        print 'iControl:setOnOff() = %s' % cmd
        self.ser.write(cmd)
        
    def isAvailable(self, cmd) :
        self.ser.write(cmd)
        while True :
            if self.ser.readline() == 'available' :
                return True
            else :
                return False
                
    def getCurrentStatus(self) :
        self.ser.write(cmd)
        while True :
            result = self.ser.readline()
            if result != '' :
                print result
                return
                
    def readLine(self) : 
        return self.ser.readline()

         
def test() :
    #print serial.tools.list_ports.comports()
    ser = serial.Serial("COM6", 9600)
    ictrl = iControl(ser)
    
    print ictrl.readLine()        

#test()

