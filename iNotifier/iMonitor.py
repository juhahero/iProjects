# This is for checking threshold
# using Observer pattern.# This is for checking threshold
# using Observer pattern.

class iMonitor :
    def __init__(self, threshold) :
        self.MAX_THRESHOLD = threshold

    def checkThreshold(self, items) :
        bRes = False
        for key, value in items :
            if(value >= self.MAX_THRESHOLD) :
                over_threshold = "%s : %s over threshold\n" % (key, value)
                print  ('=================================================\n')
                print  ("%s" %over_threshold)
                print  ('=================================================\n')
                return over_threshold
            else :
                #print 'Not over'
                pass
        return bRes

    
