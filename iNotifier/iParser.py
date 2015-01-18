import re
from iDB import *

class iParser :
    input_file = '' #default 'info.csv'
    patt_start = ''
    patt_info = ''
    patt_time = ''
    patt_choice = 0

    time = ''
    info_item = {}

    db = ''
    
    def __init__(self, db, choice) :        
        #init******************************************
        self.db = db
        self.input_file = '' #default 'info.csv'
        self.patt_start = '========================================================='
        
        #->read Time ReqEx.
        #patt_time = raw_input('Time ReqEx. [\w+\s\w+\s+[0-31]+\s+\d+:\d+:\d+\s+(KST|GMT)\s+\d{4})] : ')
        self.patt_time = '(\w+\s+\w+\s+[0-9]+\s+\d+:\d+:\d+\s+(KST|GMT)\s+\d{4})'

        #->chosed parsing ReqEx.
        self.patt_choice = choice
        if (self.patt_choice == 1) :
            print 'CputInfo : \s+(\d+\.?\d)\%\s+\d+\/([\w\.\/]+)\:\s+'
            self.patt_info = '\s+(\d+\.?\d)\%\s+\d+\/([\w\.\/]+)\:\s+'
        elif (self.patt_choice == 2) :
            print 'PowerWake : \s*(\w*WAKE_LOCK)\s+\'([\w\.\/]+)\'\s?[\w]*\s?\(uid=(\d+),\s+pid=(\d+)'
            self.patt_info = '\s*(\w*WAKE_LOCK)\s+\'([\w\.\/]+)\'\s?[\w]*\s?\(uid=(\d+),\s+pid=(\d+)'
        elif (self.patt_choice == 3) :
            print 'ProcRank : \s*(\d+)\s+(-?\d+)\s+(\d+)K?\s+(\d+)K?\s+(\d+)K?\s+(\d+)K?\s+(\d+)K?\s+([\w\.\/]+)'
            self.patt_info = '\s*(\d+)\s+(-?\d+)\s+(\d+)K?\s+(\d+)K?\s+(\d+)K?\s+(\d+)K?\s+(\d+)K?\s+([\w\.\/]+)'
        elif (self.patt_choice == 4) :
            print 'CpuFreq. : \s*(\d+)'
            self.patt_info = '\s*(\d+)'
        elif (self.patt_choice == 5) :
            print 'GpuStat. : \s*(\d+)\s+(\d+)'
            self.patt_info = '\s*(\d+)\s+(\d+)'
            
        else:
            self.patt_info = ''
            print self.patt_info


    def parse(self, obj):
        if (obj == '') :
            return

        cnt =0
        self.db.initItemsList()
        self.db.initItemList()
        data = obj
        for data in obj.splitlines() :
            rs_data = data.rstrip()
            print rs_data
            if bool(re.match(self.patt_start, rs_data)):
                print rs_data       
                              
                
            elif bool(re.match(self.patt_time, rs_data)):
                #print rs_data                        
                if (self.db.Item_list != {}):
                    self.db.insertItems(self.time, self.db.Item_list)

                self.time = rs_data
                self.db.Item_list = {} #info_db.initItemList()            

            elif bool(re.match(self.patt_info, rs_data)):
                self.info_item = re.match(self.patt_info, rs_data).groups()
                self.db.insertItem(self.info_item, self.patt_choice)

                #print info_item
            else:
                pass
           
        self.db.insertItems(self.time, self.db.Item_list)
'''
def main() :
    idb = iDB()
    iparser = iParser(idb, 1)

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
    iparser.parse(str)

    print idb.getAllItemList()

main()
'''
