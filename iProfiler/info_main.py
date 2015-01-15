import info_parse
import info_db
import csv
import collections


#init******************************************

#input*****************************************

#parse*****************************************
#collect
    #-> run power_current.sh
    #-> saving log file and collecting realtime log/parsing
#data structure********************************
info_parse.parse()
 
#data structure********************************

#output****************************************
print '****************************************'
def display_csv() :
            with open('info.csv', 'wb') as csvfile :
                    csvwriter = csv.writer(csvfile, delimiter = ',',
                                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    ### display items row
                    csvwriter.writerow([' ']+info_db.getAllItemList())
                    print info_db.getAllItemList()

                    ### display items array with time
                    sorted_items = collections.OrderedDict(sorted(info_db.Items_array.items()))
                    #for time, items in info_db.Items_array.items() :
                    for time, items in sorted_items.items() :
                        print '-------------------------------------------------------'
                        print time
                        print items
                        #csv write time + items with empty
                        #print info_db.composeOneLine(time, items)
                        csvwriter.writerow(info_db.composeOneLine(time, items))
                        
                     
            pass


display_csv()
print 'END========================================'




        
    
