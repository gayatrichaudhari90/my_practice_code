# Ticket booking system
from threading import *
class Bus:
    def __init__(self,available_seats):
        self.available_seats=available_seats
        self.l=RLock()
        
    def reserve(self,need_seats):
        print("Available seats are:",self.available_seats)
        print(self.l)
        self.l.acquire()
        self.l.acquire()
        if self.available_seats >= need_seats:
            name=current_thread().name
            print(f"{need_seats} are allocated for {name}")
            self.available_seats=need_seats
        else:
            print("Sorry!all seats are booked")
        self.l.release()
        self.l.release()

b=Bus(1)
t1=Thread(target=b.reserve,args=(1,),name="Jay")
t2=Thread(target=b.reserve,args=(1,),name="Rahul")
t1.start()
t2.start()
