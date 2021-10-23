from threading import *
from time import sleep
e=Event()
def light_switch():
    e.set()
    print("Green light is on..")
    sleep(5)
    e.clear()
    print("Red light on")
def message():
    e.wait()
    while e.is_set():
        print("You can go..")
        sleep(0.5)
t1=Thread(target=light_switch)
t2=Thread(target=message)
t1.start()
t2.start()