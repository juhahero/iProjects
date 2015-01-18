from iWorkQ import *
from Producer import *
from Consumer import *
from iCrawler import *
from iWorker import *

#main()******************************************
def main() :
    list = []
    pool = iWorkQ(list)
    crawl = iCrawler()
    worker = ''
    
    producer = Producer(pool, crawl)
    consumer = Consumer(pool, worker)

    producer.start()
    consumer.start()
    producer.join()
    consumer.join()

main()
