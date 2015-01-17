from iWorkQ import *
from Producer import *
from Consumer import *

#main()******************************************
def main() :
    list = []
    pool = iWorkQ(list)
    producer = Producer(pool)
    consumer = Consumer(pool)

    producer.start()
    consumer.start()
    producer.join()
    consumer.join()

main()
