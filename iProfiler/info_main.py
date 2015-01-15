import info_parse
import info_db
import csv
import collections
import xlwt
import os

#init******************************************
input_file = {}
output_file = '' #default 'info.csv'


#input Logs*****************************************
#->read info ReqEx.
menu_list = ['CpuInfo', 'PowerWake', 'ProcRank', 'CpuFreq', 'GpuStat', 'All']

for idx, value in enumerate(menu_list) :
        print "%d. %s" %(idx+1,value) 
        
menu = int(raw_input('Choose ReqEx.[1~6] : '))

#->read input name
def Input_file(choice) :
    global input_file
    for idx, menu in enumerate(menu_list) :
        if (idx == choice-1 or choice == 6) :            
            input_file[idx] = raw_input("%s log file : " % menu)
            print input_file[idx]
        else :
            input_file[idx] = ''
        
Input_file(menu)
    
#output*****************************************
#->read output_file_name
output_file = raw_input('output [info.xls] : ')
if (output_file == '') :
    output_file = 'info.xls'

wbk = xlwt.Workbook()

#API*****************************************
def xlwt_addsheet(menu_name) :
    wbk.add_sheet(menu_name, cell_overwrite_ok=True)
    
def xlwt_writerow(sheet, rowx, list) :
    for colx, value  in enumerate(list):        
        sheet.write(rowx, colx, value)
   
def display_xls(menu_name) :
    ### sheet
    sheet = wbk.add_sheet(menu_name, cell_overwrite_ok=True)
    ### display items row
    allItemList = info_db.getAllItemList()
    xlwt_writerow(sheet, 0, [' ']+allItemList)
    print allItemList
    
    ### display items array with time    
    sorted_items = collections.OrderedDict(sorted(info_db.Items_array.items()))
    for rowx, value in enumerate(sorted_items.items()) :
        #print '-------------------------------------------------------'
        #print time
        #print items

        #csv write time + items with empty
        #print info_db.composeOneLine(time, items)
        xlwt_writerow(sheet, rowx+1, info_db.composeOneLine(value[0], value[1], allItemList))
    
def display_All() :
    global input_file
    for idx, value in enumerate(input_file) :
        print input_file[idx]
        if (os.path.isfile(input_file[idx]) == True) :            
            info_parse.init_parse(idx+1)
            info_parse.parse(input_file[idx])
            display_xls(menu_list[idx])
        else:
            pass        
        
#parse*****************************************


#collect
    #-> run power_current.sh
    #-> saving log file and collecting realtime log/parsing

#data structure********************************

#output****************************************
print '****************************************'
display_All()    
wbk.save(output_file)
print 'END========================================'




        
    
