marks=float(input("ENTER YOUR MARKS:"))
if marks<=100 and marks>=90:
    print("YOUR GRADE IS A")
elif marks<=89 and marks>=75:
    print("YOUR GRADE IS B")
elif marks<=74 and marks>=60:
    print("YOUR GRADE IS C")
elif marks<=59 and marks>=40:
    print("YOUR GRADE IS D")
elif marks<=39 and marks>=0:
    print("YOU ARE FAILED")
else:
    print("INVALID MARKS")