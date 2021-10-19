# Bank application/ATM System

class BalanceExceptionError(Exception):
    pass

def withdraw():
    money = 10000
    amt=float(input("Enter amount to withdraw:"))
    try:
        balance = money-amt
        if balance<1000 and balance>0:
            raise BalanceExceptionError("You can't withdraw")
        elif balance<=0:
            raise BalanceExceptionError("insufficient balance")
    except BalanceExceptionError as obj:
        print(obj)
    else:
        money = money-amt
        print("Available amount is:",money)

withdraw()
