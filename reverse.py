'''name=input("Enter string:")
print("Original string is:",name)
r_name=""
count=len(name)
while count>0:
    r_name=r_name+name[count-1]
    count=count-1
print('reversed string:',r_name)
'''
str1=input("Enter the string:")
print("Original string is:",str1)
r_name=""
for char in str1:
    r_name=char+r_name
print("reversed string is:",r_name)
