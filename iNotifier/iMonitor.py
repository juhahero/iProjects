# This is for checking threshold
# using Observer pattern.# This is for checking threshold
# using Observer pattern.

class iMonitor :
    def __init__(self, threshold) :
        self.MAX_THRESHOLD = threshold

    def checkThreshold(self, items, thold) :
        bRes = False
        for key, value in items :
            if(value >= thold) :
                print 'overheat'
                return True
            else :
                print 'Not over'
        return bRes

    
