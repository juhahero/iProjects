from socket import *

csock = socket(AF_INET, SOCK_STREAM)
csock.connect(('localhost', 8001))
csock.send('Hi')
csock.close()
