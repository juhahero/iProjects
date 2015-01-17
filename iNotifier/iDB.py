class iDB :

    def __init__(self) :        
        self.Item_list = {}
        self.Items_array = {}
        #Item_All = {}
        self.EMPTY = 0

    def checkDuplicatedItem(self, list, item) :
        #print list
        bDup = False
        
        for e in list :
            #print e
            if(e == item) :
                #print 'True'
                return True
        return bDup
            
            
    def getAllItemList(self) :
        list = []
        for time, items in self.Items_array.items() :

            #print '*********************************'
            #print items
            for key, val in items.items() :
                #print key
                if list == [] :
                    list.append(key)
                    continue
                
                #print list
                if(self.checkDuplicatedItem(list, key) == False) :
                    list.append(key)
            #print list
            
        return list

    def checkItems(self, key, list) :
        index = 0
        #list = getAllItemList()
        for name in list :        
            if (name == key) :
                return index
            index += 1
        return index

    def composeOneLine(self, time, items, Item_All) :
        #Item_All = getAllItemList()
        
        list = [self.EMPTY for _ in range(len(Item_All)+1)] # +1 : time 
        list[0] = time

        for key, val in items.items() :
            idx = self.checkItems(key, Item_All)
            if(idx < len(Item_All)) :
                list[idx+1] = val
        return list
            
    def composeFullLines(self) :
        list = []
        for time, items in self.Items_array.items() :
            list.append(self.composeOneLine(time, items))
        return list

    def findByPid(self, pid) : #not yet... no pid table
        list = []
        for time, items in self.Items_array.items() :
            for key, val in items.items() :
                if(key == pid) :
                    list.append(val)
            list.append('0')
        return list

    def findByName(self, name) :
        list = []
        for time, items in self.Items_array.items() :
            for key, val in items.items() :
                if(key == name) :
                    list.append(val)
            list.append('0')
        return list

    def findByTime(self, time) :
        for key, items in self.Items_array.items() :
            if(key == time) :
                return items
            
    def insertItem(self, item, patt_choice) :
        #print patt_choice
        if (patt_choice == 1) : #cpuinfo
            self.Item_list[item[1]] = float(item[0])
        elif (patt_choice == 2) : #powerwake
            self.Item_list[item[1]] = float(item[3])
        elif (patt_choice == 3) : #procrank
            self.Item_list[item[7]] = float(item[3])
        elif (patt_choice == 4) : #cpufreq
            self.Item_list['cpufreq'] = float(item[0])
        elif (patt_choice == 5) : #gpustat
            self.Item_list['gpustat1'] = float(item[0])
            self.Item_list['gpustat2'] = float(item[1])
        else :
            self.Item_list[item[1]] = float(item[0])
        

    def insertItems(self, time, Items) :
        self.Items_array[time] = Items
        

    def initItemList(self) :
        self.Item_list = {}

    def initItemsList(self) :
        self.Items_array = {}

    def dispItemList(self) :
        print self.Item_list

    def dispItemsList(self) :
        print self.Items_array
        

