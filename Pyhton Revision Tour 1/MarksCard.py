
marks = int(input("Enter your score: "))
#Type casting

if marks <35:
    print("You are fail")
elif marks >=35 and marks<50 :
    print("Pass Class")
elif marks >= 50 and marks < 65:
    print("Second Class")
elif marks >= 65 and marks < 85:
    print("First Class")
elif marks >= 85 and marks <= 100:
    print("Top Class")
else:
    print("Contact School admin")
