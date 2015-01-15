Item_list = {}
Items_array = {}
#Item_All = {}
EMPTY = 0

def checkDuplicatedItem(list, item) :
    #print list
    bDup = False
    
    for e in list :
        #print e
        if(e == item) :
            #print 'True'
            return True
    return bDup
        
            
def getAllItemList() :
    list = []
    for time, items in Items_array.items() :

        #print '*********************************'
        #print items
        for key, val in items.items() :
            #print key
            if list == [] :
                list.append(key)
                continue
            
            #print list
            if(checkDuplicatedItem(list, key) == False) :
                list.append(key)
        #print list
        
    return list
def checkItems(key, list) :
    index = 0
    #list = getAllItemList()
    for name in list :        
        if (name == key) :
            return index
        index += 1
    return index

def composeOneLine(time, items, Item_All) :
    #Item_All = getAllItemList()
    
    list = [EMPTY for _ in range(len(Item_All)+1)] # +1 : time 
    list[0] = time

    for key, val in items.items() :
        idx = checkItems(key, Item_All)
        if(idx < len(Item_All)) :
            list[idx+1] = val
    return list
        
def composeFullLines() :
    list = []
    for time, items in Items_array.items() :
        list.append(composeOneLine(time, items))
    return list

def findByPid(pid) : #not yet... no pid table
    list = []
    for time, items in Items_array.items() :
        for key, val in items.items() :
            if(key == pid) :
                list.append(val)
        list.append('0')
    return list

def findByName(name) :
    list = []
    for time, items in Items_array.items() :
        for key, val in items.items() :
            if(key == name) :
                list.append(val)
        list.append('0')
    return list

def findByTime(time) :
    for key, items in Items_array.items() :
        if(key == time) :
            return items
        
def insertItem(item, patt_choice) :
    #print patt_choice
    if (patt_choice == 1) : #cpuinfo
        Item_list[item[1]] = float(item[0])
    elif (patt_choice == 2) : #powerwake
        Item_list[item[1]] = float(item[3])
    elif (patt_choice == 3) : #procrank
        Item_list[item[7]] = float(item[3])
    elif (patt_choice == 4) : #cpufreq
        Item_list['cpufreq'] = float(item[0])
    elif (patt_choice == 5) : #gpustat
        Item_list['gpustat1'] = float(item[0])
        Item_list['gpustat2'] = float(item[1])
    else :
        Item_list[item[1]] = float(item[0])
    

def insertItems(time, Items) :
    Items_array[time] = Items
    

def initItemList() :
    global Item_list
    Item_list = {}

def initItemsList() :
    global Items_array
    Items_array = {}

def dispItemList() :
    print Item_list

def dispItemsList() :
    print Items_array
    

