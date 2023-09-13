n=input("Enter a value:")
d={31:["januvary","march","may","july","august","october","december"],30:["april","june","September","november"],28:"february",29:"february"}
if (n in d[31]):
    print("31 days")
elif (n in d[30]):
    print("30 days")
elif (n in d[28]):
    print("28 days")
else:
    print("invalid input")
    