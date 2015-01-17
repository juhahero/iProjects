from iWorkQ import *
from Producer import *
from Consumer import *
from iCrawler import *

#main()******************************************
def main() :
    list = []
    pool = iWorkQ(list)
    crawl = iCrawler()
    
    producer = Producer(pool, crawl)
    consumer = Consumer(pool)

    producer.start()
    consumer.start()
    producer.join()
    consumer.join()

main()
