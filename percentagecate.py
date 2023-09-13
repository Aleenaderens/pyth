n=int(input("Enter a value:"))
if (n<40):
    print("Failed")
elif (n>=40) and (n<55):
    print("fair")
elif (n>=55) and (n<65):
    print("Good")
elif (n>=65):
    print("Excellent")
else:
    print("invalid input")