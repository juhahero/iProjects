import xlwt
import info_parse
import info_db
import os
import collections

#output*****************************************
wbk = xlwt.Workbook()

#xlwt API*****************************************
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
        #print value

        #csv write time + items with empty
        #print info_db.composeOneLine(time, items)
        xlwt_writerow(sheet, rowx+1, info_db.composeOneLine(value[0], value[1], allItemList))

def display_All(menu_list, input_file, output_file) :
    #global input_file
    global wbk
    for idx, value in enumerate(input_file) :
        print input_file[idx]
        if (os.path.isfile(input_file[idx]) == True) :            
            info_parse.init_parse(idx+1)
            info_parse.parse(input_file[idx])
            display_xls(menu_list[idx])
        else:
            pass        
        
    wbk.save(output_file) 
print 'END========================================'




        
    
