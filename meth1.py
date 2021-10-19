class OverloadDemo:
    def sum(self,x=None,y=None,z=None):
        if x!=None and y!=None and z!=None:
            s=x+y+z
            print("sum=",s)

        elif x!=None and y!=None:
            s=x+y
            print('sum=',s)

od=OverloadDemo()
od.sum(10,20)
od.sum(10,20,30)