'''
continually removes the item at the end of the list and puts
it at the beginning num times.
'''
from queue import Queue

def hot_potato(namelist, num):
    simqueue= Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()

print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))
