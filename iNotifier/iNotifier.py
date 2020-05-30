from iWorkQ import *
from Producer import *
from Consumer import *
from iCrawler import *
from iWorker import *

#input Logs*****************************************
#->read info ReqEx.
menu_list = ['CpuInfo', 'PowerWake', 'ProcRank', 'CpuFreq', 'GpuStat', 'All']
cmd_list = ['adb shell dumpsys cpuinfo',
            'adb shell dumpsys power',
            'adb shell procrank',
            'adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq',
            'cat /sys/class/kgsl/kgsl-3d0/gpubusy'
            ]
threshold_list = [90, 0, 100000, 1190400, 1005438]

for idx, value in enumerate(menu_list) :
        print ("%d. %s" %(idx+1,value))
        
menu = int(input('Choose ReqEx.[1~6] : '))
           
#main()******************************************
def main() :
    list = []
    pool = iWorkQ(list)
    crawl = iCrawler(cmd_list[menu-1])
    worker = iWorker(menu, '', threshold_list[menu-1])
    
    producer = Producer(pool, crawl)
    consumer = Consumer(pool, worker)

    producer.start()
    consumer.start()
    producer.join()
    consumer.join()

main()
