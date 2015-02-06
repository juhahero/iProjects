# This is Request Handler extended StreamRequestHandler
# referenced from 'www.FREELEC.co.kr'

import socket
from SocketServer import ThreadingTCPServer, StreamRequestHandler

class iRequestHandler(StreamRequestHandler) :      
    def handle(self) :
        print 'connection from', self.client_address
        conn = self.request

        while True :
            msg = conn.recv(1024)
            if not msg :
                conn.close()
                print self.client_address, 'disconnected'
                break;

            print self.client_address, msg

'''
def test() :
    server = ThreadingTCPServer(('',8001), iRequestHandler)
    print 'listening on port', 8001

    server.serve_forever()

test()
'''
# This is Request Handler extended StreamRequestHandler
# referenced from 'www.FREELEC.co.kr'

import socket
from SocketServer import ThreadingTCPServer, StreamRequestHandler

import BaseHTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
import time

PORT = 8000

class iSOCKRequestHandler(StreamRequestHandler) :      
    def handle(self) :
        print 'connection from', self.client_address
        conn = self.request

        while True :
            msg = conn.recv(1024)
            if not msg :
                conn.close()
                print self.client_address, 'disconnected'
                break;

            print self.client_address, msg

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
        server = ThreadingTCPServer(('',PORT), iRequestHandler)
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
    
CGITest()

