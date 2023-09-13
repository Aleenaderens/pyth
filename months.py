n=int(input("Enter a value:"))
d={31:["januvary","march","may","july","august","october","december"],30:["april","june","September","november"],28:"february",29:"february"}
if (n==31):
    print(d[31])
elif (n==30):
    print(d[30])
elif (n==28):
    print(d[28])
else:
    print("invalid input")