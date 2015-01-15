import re
import info_db
import os

#init******************************************
input_file = '' #default 'info.csv'
patt_start = ''
patt_info = ''
patt_time = ''
patt_choice = 0



#->read start ReqEx.
#patt_start = raw_input('start ReqEx.[=========================================================] : ')
if (patt_start == '') :
    patt_start = '========================================================='

#->read Time ReqEx.
#patt_time = raw_input('Time ReqEx. [\w+\s\w+\s+[0-31]+\s+\d+:\d+:\d+\s+(KST|GMT)\s+\d{4})] : ')
if (patt_time == '') :
    patt_time = '(\w+\s+\w+\s+[0-9]+\s+\d+:\d+:\d+\s+(KST|GMT)\s+\d{4})'
    
def init_parse(menu) :
    global patt_choice
    global patt_info
    
    patt_choice = menu
    if (patt_choice == 1) :
        print 'CputInfo : \s+(\d+\.?\d)\%\s+\d+\/([\w\.\/]+)\:\s+'
        patt_info = '\s+(\d+\.?\d)\%\s+\d+\/([\w\.\/]+)\:\s+'
    elif (patt_choice == 2) :
        print 'PowerWake : \s*(\w*WAKE_LOCK)\s+\'([\w\.\/]+)\'\s?[\w]*\s?\(uid=(\d+),\s+pid=(\d+)'
        patt_info = '\s*(\w*WAKE_LOCK)\s+\'([\w\.\/]+)\'\s?[\w]*\s?\(uid=(\d+),\s+pid=(\d+)'
    elif (patt_choice == 3) :
        print 'ProcRank : \s*(\d+)\s+(-?\d+)\s+(\d+)K?\s+(\d+)K?\s+(\d+)K?\s+(\d+)K?\s+(\d+)K?\s+([\w\.\/]+)'
        patt_info = '\s*(\d+)\s+(-?\d+)\s+(\d+)K?\s+(\d+)K?\s+(\d+)K?\s+(\d+)K?\s+(\d+)K?\s+([\w\.\/]+)'
    elif (patt_choice == 4) :
        print 'CpuFreq. : \s*(\d+)'
        patt_info = '\s*(\d+)'
    elif (patt_choice == 5) :
        print 'GpuStat. : \s*(\d+)\s+(\d+)'
        patt_info = '\s*(\d+)\s+(\d+)'
        
    else:
        patt_info = patt_choice
        print patt_info

time = ''
info_item = {}
def parse(input_file):
    if (os.path.isfile(input_file) == False) :
        return
    
    f = open(input_file)
    cnt =0
    info_db.initItemsList()
    info_db.initItemList()
    data = f.readline()
    while data:
        rs_data = data.rstrip()
        if bool(re.match(patt_start, rs_data)):
            #print rs_data       
            pass              
            
        elif bool(re.match(patt_time, rs_data)):
            #print rs_data                        
            if (info_db.Item_list != {}):
                info_db.insertItems(time, info_db.Item_list)

            time = rs_data
            info_db.Item_list = {} #info_db.initItemList()            

        elif bool(re.match(patt_info, rs_data)):
            info_item = re.match(patt_info, rs_data).groups()
            info_db.insertItem(info_item, patt_choice)

            #print info_item
        else:
            pass

        data = f.readline()
        
    info_db.insertItems(time, info_db.Item_list)
    f.close()

