# Producer consumer program
from threading import Thread,Condition
from time import sleep
mylist=[]
c=Condition()
def produce():
    c.acquire()
    for i in range(1,6):
        mylist.append(i)
        sleep(1)
        print("Item produce:",i)
    c.notify_all()
    c.release()

def consume():
    c.acquire()
    c.wait(timeout=-1)
    c.release()
    for i in range(5):
        sleep(0.5)
        print("Item consumed:",mylist[i])

def consumer2():
    c.acquire()
    c.wait(timeout=-1)
    c.release()
    for i in range(5):
        sleep(0.5)
        print("Item consumed:",mylist[i])

t1=Thread(target=produce)
t2=Thread(target=consume)
t3=Thread(target=consumer2)
t1.start()
t2.start()
t3.start()