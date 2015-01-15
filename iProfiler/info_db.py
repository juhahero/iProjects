Item_list = {}
Items_array = {}
#Item_All = []
EMPTY = '0'

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
def checkItems(key) :
    index = 0
    list = getAllItemList()
    for name in list :        
        if (name == key) :
            return index
        index += 1
    return index

def composeOneLine(time, items) :
    list = [EMPTY for _ in range(len(getAllItemList())+1)] # +1 : time 
    list[0] = time

    for key, val in items.items() :
        idx = checkItems(key)
        if(idx < getAllItemList()) :
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
        
def insertItem(item) :
    Item_list[item[1]] = item[0]
    pass

def insertItems(time, Items) :
    Items_array[time] = Items
    pass

def initItemList() :
    Item_list = {}

def initItemsList() :
    Items_array = {}

def dispItemList() :
    print Item_list

def dispItemsList() :
    print Items_array
    

