class FiveDivisionError(Exception):
    pass
num1=int(input("Enter a number:"))
num2=int(input("Enter second number:"))
try:
    if num2 == 5:
        raise FiveDivisionError("cannot divide by five")

    else:
        print(num1/num2)

except FiveDivisionError as obj:
    print(obj)