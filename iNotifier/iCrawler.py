# This is collecting data
# using Master-Slave pattern

import subprocess

class iCrawler :
    """
    crwaling... realtime log
                logfile / website / smartsensor
    """
    
    crwal_data = ''
    def __init__(self) :
        pass

    def crawledData(self) :
        #ex) read data from cmd( or file)

        output = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
            
        print "crawledData = %s" % output
        data = output
        
        if data != '':
            self.crwal_data = data.rstrip()

        return self.crwal_data

'''    
def test() :
    craw = iCrawler()
    craw.crawledData()

test()
'''
