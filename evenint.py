i=0
a=int(input("Enter the limit:"))
li=[]
while i<a:
    n=int(input("Enter the number: "))
    li.append(n)
    i=i+1
print(li)
j=0
newli=[]
while j<a:
    if li[j]%2==0:
      newli.append(li[j])
    j=j+1
print(newli)