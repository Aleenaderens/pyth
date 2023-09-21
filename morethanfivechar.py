n=(input("enter the word:"))
li=[]
x=n.split()
print(x)
i=0
while(i<len(x)):
    if(len(x[i])>=5):
        li.append(x[i])
    i=i+1
print(li)