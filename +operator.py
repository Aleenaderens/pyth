a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=(input("Enter operator:"))
if (c=="+"):
    print("your answer is",a+b)
elif (c=="-"):
    print("your answer is",a-b)
elif (c=="*"):
    print("your answer is",a*b)
elif(c=="/"):
    print("your answer is",a/b)
else:
    print("Invalid input")