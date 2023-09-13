units=int(input("Enter a value:"))
if (units<=100):
    print("no charge")
elif units>=100 and  units<=200:
     x=(units-100)*5 
     print(x)
elif units>=200:
     x=(500+(units-200)*10)
     print(x)
else:
     print("Invalid input")