n=int(input("ENTER YOUR NUMBER:"))
i=1
sum=0

while i<=n:
    if i%2==0:
     i=i+1
     continue

    print(i) 
    sum=sum+i
    i=i+1  

print("THE SUM OF NUMBERS TILL YOUR GIVEN RANGE IS:",sum) 
    

    