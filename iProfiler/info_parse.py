import re
import info_db

#regular exp. for cpuinfo log
patt_start = '========================================================='
patt_info = '\s+(\d+\.?\d)\%\s+\d+\/([\w.]+)\:\s+'
patt_time = '(\w+\s\w+\s+[0-31]+\s+\d+:\d+:\d+\s+(KST|GMT)\s+\d{4})'

time = ''
info_item = {}

def parse():    
    f = open('info.log')
    cnt =0
    data = f.readline()
    while data:
        rs_data = data.rstrip()
        if bool(re.match(patt_start, rs_data)):
            #print rs_data
            pass              
            
        elif bool(re.match(patt_time, rs_data)):
            #print rs_data
            time = rs_data
            #power_db.dispItemList()
            info_db.insertItems(time, info_db.Item_list)            
            info_db.Item_list = {} #info_db.initItemList()            

        elif bool(re.match(patt_info, rs_data)):
            info_item = re.match(patt_info, rs_data).groups()
            info_db.insertItem(info_item)            
            #print info_item
        else:
            pass

        data = f.readline()
    f.close()

