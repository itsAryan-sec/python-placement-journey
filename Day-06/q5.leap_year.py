a=int(input("ENTER THE YEAR:"))
if a%400==0:
    print(" THEY EAR",a,"IS A LEAP YEAR")
elif a%100==0:
    print("THE YEAR",a,"IS NOT A LEAP YEAR")
elif a%4==0:
    print("THEY EAR",a,"IS A LEAP YEAR")
else:
    print("THE YEAR",a,"IS NOT A LEAP YEAR")
