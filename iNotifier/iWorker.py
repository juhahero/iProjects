# working with parsing / DB
# using thread pool

import threading
import time
from iDB import *
from iParser import *
from iMonitor import *
from iTwit import *

class iWorker :
    def __init__(self, type, obj, threshold) :
        #threading.Thread.__init__(self)
        self.db = iDB()
        self.parser = iParser(self.db, type)
        self.monitor = iMonitor(threshold)
        self.twit = iTwit('doradoli')
        self.job = obj
        self.threshold = threshold

    def runJob(self, job) :
        self.parser.parse(job)
        print self.db.Item_list.items()
        sCheck = self.monitor.checkThreshold(self.db.Item_list.items())
        if (sCheck) :
            try :
                self.twit.sendDM(sCheck)
            except TweepError as e :
                print "Exception : %s" % e.args[0]
        else :
            #self.twit.sendDM('NOT cpu overheat')
            pass            
        time.sleep(1)
'''
def test() :
    str = """
Sat Jan 31 19:30:02 GMT 1970
Load: 13.26 / 13.47 / 11.88
CPU usage from 116890ms to 56891ms ago with 99% awake:
  96% 1023/system_server: 0.1% user + 0% kernel / faults: 35 minor
  0.1% 336/atd: 0% user + 0.1% kernel
  0.1% 1254/com.android.systemui: 0.1% user + 0% kernel / faults: 1 minor
  0.1% 2238/mpdecision: 0% user + 0.1% kernel
  0% 3/ksoftirqd/0: 0% user + 0% kernel
  0% 383/kworker/0:3: 0% user + 0% kernel
  0% 173/mmcqd/1: 0% user + 0% kernel
  0% 563/kernel_logger: 0% user + 0% kernel
  0% 320/thermal-engine: 0% user + 0% kernel
  0% 550/logcat: 0% user + 0% kernel
  0% 6669/kworker/u:5: 0% user + 0% kernel
  0% 6715/adbd: 0% user + 0% kernel
  0% 7/kworker/u:0H: 0% user + 0% kernel
  0% 180/flush-179:0: 0% user + 0% kernel
  0% 187/jbd2/mmcblk0p34: 0% user + 0% kernel
  0% 234/charger_monitor: 0% user + 0% kernel
  0% 1248/MC_Thread: 0% user + 0% kernel
  0% 1419/wpa_supplicant: 0% user + 0% kernel
  0% 2283/kworker/0:2H: 0% user + 0% kernel
3.6% TOTAL: 1.3% user + 2.2% kernel + 0% iowait + 0% softirq
"""

    iwork = iWorker(1, str)
    iwork.runJob(str)

test()
'''
