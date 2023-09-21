a=int(input("Enter a limit:"))
i=0
li=[]
while i<a:
    n=input("enter word:")
    li.append(n)
    i=i+1
print(li)
j=0
newli=[]
while j<a:
    newli.append(li[j].capitalize())
    j=j+1
print(newli)

   
      