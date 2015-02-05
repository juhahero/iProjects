# This is Server referenced from 'www.FREELEC.co.kr'

import socket
from SocketServer import ThreadingTCPServer, StreamRequestHandler
from iRequestHandler import *

class iServer :

    def __init__(self, port, rhdlr) :
        self.PORT = port
        self.server = ThreadingTCPServer(('', port), rhdlr)
        print 'listening on port', port

        self.server.serve_forever()


'''
def test() :
    server = iServer(8001, iRequestHandler)


test()
'''    
    
    

    
