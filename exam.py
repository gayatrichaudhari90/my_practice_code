#WAP for mim,maxi,sum
l=[]
while(1):
    num=int(input("Enter number:"))
    l.append(num)
    ans=input("Do you want to enter another number:(enter 'y')")
    if ans!='y':
        break

def min1(l):
    minimum=l[0]
    for n in l:
        if n < minimum:
            minimum = n
    return minimum

def max1(l):
    maximum = l[0]
    for n in l:
        if n > maximum:
            maximum = n
    return maximum

def sum1(l):
    addition = 0
    for n in l:
        addition = addition+n
    return addition

while 1:
    print("Select:\n1.find maximum \n2.find minimum \n3.find sum")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Maximum value is:",max1(l))
    elif choice==2:
        print("Minimum value is:",min1(l))
    elif choice==3:
        print("Sum is:",sum1(l))
    else:
        print("Invalid choice")
    ans=input("Do you want to continue?:(enter 'y')")
    if ans!='y':
        break
















        
