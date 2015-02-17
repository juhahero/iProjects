# This is Request Handler extended StreamRequestHandler
# referenced from 'www.FREELEC.co.kr'

import socket
from SocketServer import ThreadingTCPServer, StreamRequestHandler

import BaseHTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
import time

from ..Light.Light import *
from ..Light.LightOnCmd import *
from ..WMS.Work import *
from ..WMS.iWMSInstance import *

import serial

PORT = 8000

class iSOCKRequestHandler(StreamRequestHandler) :      
    def handle(self) :
        print 'connection from', self.client_address
        conn = self.request

        while True :
            msg = conn.recv(1024)
            if not msg :
                conn.close()
                print self.client_address, 'disconnected\n'
                break;

            elif msg == 'ON' :
                ser = serial.Serial("COM6", 9600)
                ictrl = iControl(ser)
                light = Light(ictrl)
                cmd = LightOnCmd(light)
                work = Work(cmd)
                wms = iWMSInstance()
                wms.execute(work)

            print self.client_address, msg
            print '\n'

class iHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler) :
    def do_GET(self) :
        if self.path != '/' :
            self.send_error(404, 'File not found')
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.printPage()

    def printPage(self) :
        t = time.asctime()

        self.wfile.write('<html><body> access time : <b>%s<b></body></html>' % t)

class iCGIRequestHandler(CGIHTTPRequestHandler) :
    cgi_directories = ["/cgi"]
    def do_GET(self) :
        if self.path != '/' :
            self.send_error(404, 'File not found')
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.printPage()

    def printPage(self) :
        t = time.asctime()

        self.wfile.write('<html><body> access time : <b>%s<b></body></html>' % t) 
# =================> TEST
def SOCKTest() :
    try :
        server = ThreadingTCPServer(('',PORT), iSOCKRequestHandler)
        print 'listening on port', PORT
    
        server.serve_forever()
    except KeyboardInterrupt :
        server.socket.close()
        print 'server closed'    
    
def HTTPTest() :
    try :
        server = BaseHTTPServer.HTTPServer(('', PORT), iHTTPRequestHandler)
        print 'listening on port', PORT

        server.serve_forever()
    except KeyboardInterrupt :
        server.socket.close()
        print 'server closed'

def CGITest() :
    #handler = CGIHTTPServer.CGIHTTPRequestHandler
    #handler.cgi_directories = ['/cgi']
    try :
        server=BaseHTTPServer.HTTPServer(('', PORT), iCGIRequestHandler)
        print 'listening on port', PORT
        server.serve_forever()
    except KeyboardInterrupt :
        server.socket.close()
        print 'server closed'

def WMS_init() :
    list = []
    wq = iWorkQ(list)
    
    worker = iWorkerThread('test', wq)
    
    thList = []
    wms = iWMSInstance()
    wms.init(wq, thList)
    wms.register(worker)

#WMS_init()
#SOCKTest()

