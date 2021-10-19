jbk={'nikhil':12000,'akshay':11000,'shantanu':13000,'roshan':14000}
python_fees=15000
while 1:
    print("Menu:")
    print("1.Display fees:")
    print("2.Update fees:")
    print("3.Delete records:")
    print("4.Display records:")
    print("5.new student:")
    print("6.clear all records:")
    choice=int(input("Enter your choice:"))
    if choice==1:
        list_of_students=list(jbk.keys())
        name=input("Enter your name:")
        if name in list_of_students:
            print(f"fees of {name}:{jbk[name]}")
        else:
            print("No such student")
    elif choice==2:
        list_of_student=list(jbk.keys())
        name=input("Enter the name of student for updating fees:")
        if name in list_of_students:
            pay=float(input("Enter amount to pay:"))
            jbk[name]=jbk[name]-pay
            print("Successfully updated")            
    elif choice==3:
        name=input("Enter the name of student who is leaving class:")
        if jbk[name]==0:
            del jbk[name]
        else:
            print("You haven't paid the fees")
    elif choice==4:
        print("Name of student  fees")
        for name,fees in jbk.items():
            print(name,"----->",fees)
    elif choice==5:
        name=input("Enter your name:")
        jbk[name]=python_fees
    elif choice==6:
        ans=input("Are you sure you want to clear all records?(enter only'y'for yes)")
        if ans=='y':
            jbk.clear()
            print("Successfully cleared")
        else:
            print("Invalid choice")
            ans=input("Do you want to continue:(y/n)")
            ans=ans.lower()
            if ans!='y':
                break
            

    
    
            
    
