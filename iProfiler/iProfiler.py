import info_parse
import info_db
import csv
import collections

import os
import out_xls
import out_html

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
output_file = raw_input('output [info.html] : ')
if (output_file == '') :
    output_file = 'info.html'

out_html.f_name = output_file 
#parse*****************************************


#collect
    #-> power_current.sh 
    #-> saving logfile and realtime collecting /parsing
#data structure********************************

#output****************************************
print '****************************************'
#out_xls.display_All(menu_list, input_file, output_file)
out_html.display_All(menu_list, input_file, output_file)
print 'END========================================'




        
    
