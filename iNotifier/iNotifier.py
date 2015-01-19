from iWorkQ import *
from Producer import *
from Consumer import *
from iCrawler import *
from iWorker import *

#input Logs*****************************************
#->read info ReqEx.
menu_list = ['CpuInfo', 'PowerWake', 'ProcRank', 'CpuFreq', 'GpuStat', 'All']


for idx, value in enumerate(menu_list) :
        print "%d. %s" %(idx+1,value) 
        
menu = int(raw_input('Choose ReqEx.[1~6] : '))

#main()******************************************
def main() :
    list = []
    pool = iWorkQ(list)
    crawl = iCrawler()
    worker = iWorker(menu, '')
    
    producer = Producer(pool, crawl)
    consumer = Consumer(pool, worker)

    producer.start()
    consumer.start()
    producer.join()
    consumer.join()

main()
