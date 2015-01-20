# This is collecting data
# using Master-Slave pattern

import subprocess

class iCrawler :
    """
    crwaling... realtime log
                logfile / website / smartsensor
    """
    
    crwal_data = ''
    def __init__(self, cmd) :
        self.cmd = cmd

    def crawledData(self) :
        #ex) read data from cmd( or file)

        date = subprocess.Popen('date', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
        result = subprocess.Popen(self.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()

        output = "%s%s" %(date, result)
        print "crawledData = %s" % output
        data = output
        
        if data != '':
            self.crwal_data = data.rstrip()

        return self.crwal_data

'''    
def test() :
    craw = iCrawler()
    craw.crawledData('adb shell dumpsys cpuinfo')

test()
'''
