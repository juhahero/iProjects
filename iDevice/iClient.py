from socket import *

csock = socket(AF_INET, SOCK_STREAM)
csock.connect(('localhost', 8000))
csock.send('ON')
csock.close()
