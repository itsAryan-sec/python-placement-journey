a=int(input("ENTER YOUR NUMBER:"))
b=input("ENTER YOUR OPERATOR:")
c=int(input("ENTER YOUR NUMBER:"))
if b == '+':
    print(a+c)
elif b=='-':
    print(a-c) 
elif b=='*':
    print(a*c)
elif b=='/':
    print(a/c)
elif b=='%':
    print(a%c)
else:
    print("ENTER A VALID OPERATOR")
    