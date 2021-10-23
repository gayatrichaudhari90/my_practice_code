from threading import Thread,current_thread
class MyExam:
    def solve(self):
        self.q1()
        self.q2()
        self.q3()
    def q1(self):
        print("Question 1 solved",current_thread().name)
    def q2(self):
        print("Question 2 solved",current_thread().name)
    def q3(self):
        print("Question 3 solved",current_thread().name)

m=MyExam()
t1 =Thread(target=m.solve,name="saurav")
t2 =Thread(target=m.solve,name="Vijay")
t1.start()
t2.start()
            