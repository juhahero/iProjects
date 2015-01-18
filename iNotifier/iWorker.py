# working with parsing / DB
# using thread pool

import threading
import time
from iDB import *
from iParser import *

class iWorker(threading.Thread) :
    def __init__(self, type, obj) :
        threading.Thread.__init__(self)
        self.db = iDB()
        self.parser = iParser(self.db, type)
        self.job = obj

    def run(self) :
        self.parser.parse(self.job)
        print self.db.getAllItemList()
        time.sleep(1)

    def setJob(self, obj) :
        self.job = obj
        
'''
def test() :
    str = """
Sat Jan 31 19:30:02 GMT 1970
Load: 13.26 / 13.47 / 11.88
CPU usage from 116890ms to 56891ms ago with 99% awake:
  0.2% 1023/system_server: 0.1% user + 0% kernel / faults: 35 minor
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
    iwork.start()
    iwork.join()

test()
'''
