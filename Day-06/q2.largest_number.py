a=int(input("ENTER FIRST NUMBER:"))
b=int(input("ENTER SECOND NUMBER:"))
c=int(input("ENTER THIRD NUMBER:"))

if a>=b  and a>=c:
    print(a," is greater")
elif b>=c and b>=a:
    print(b,"is greater")

else:
    print(c,"is greater")
