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
