import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from collections import deque
import random
MAX_X = 100
MAX_Y = 1000

line = deque([0.0]*MAX_X, maxlen=MAX_X)

def update(fn, l2d):
    #simulate data from serial within +-5 of last datapoint
    dy = random.randint(-5, 5)
    #add new point to deque
    line.append(line[MAX_X-1]+dy)
    # set the l2d to the new line coords
    # args are ([x-coords], [y-coords])
    l2d.set_data(range(0,60), line)

fig = plt.figure()
# make the axes revolve around [0,0] at the center
# instead of the x-axis being 0 - +100, make it -50 - +50
# ditto for y-axis -512 - +512
a = plt.axes(xlim=(-(MAX_X/2),MAX_X/2), ylim=(-(MAX_Y/2),MAX_Y/2))
# plot an empty line and keep a reference to the line2d instance
l1, = a.plot([], [])
ani = anim.FuncAnimation(fig, update, fargs=(l1,), interval=50)
 
 
plt.show()

'''
plot_data = [
    ["2013-03-18 15:31:36.617",0],
    ["2013-03-18 15:31:38.511",15],
    ["2013-03-18 15:31:40.324",30],
    ["2013-03-18 15:31:42.144",35],
    ["2013-03-18 15:31:43.961",60]
]

lstX = []
lstY = []

plt.ion()

fig = plt.figure()
sf = fig.add_subplot(111)

#plt.xlim([0,60])
#plt.ylim([300, 1000])

line1, = sf.plot(lstX, lstY, 'r-')
#line1, = sf.plot(lstX,lstY,linestyle='-', marker='o', label="value")
for line in plot_data:
    times = dt.datetime.strptime(line[0],'%Y-%m-%d %H:%M:%S.%f')
    lstX.append(times)
    lstY.append(line[1])

    print ('time:%s, value:%d' % (times, line[1]))

    #plt.plot(lstX,lstY,linestyle='-', marker='o', label="value")
    
    line1.set_xdata(lstX)
    line1.set_ydata(lstY)

    plt.draw(), plt.pause(0.00001)
'''
