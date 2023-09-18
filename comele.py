l1=[]
a=int(input("enter limit:"))
i=0
while(i<a):
    n=int(input("Enter list1:"))
    l1.append(n)
    i=i+1
l2=[]
# b=int(input("enter limit:"))
j=0
while(j<a):
    n=int(input("Enter list2:"))
    l2.append(n)
    j=j+1
print(l1)
print(l2)
k=0
l3=[]
while (k<a):
    if l1[k] in l2:
        l3.append(l1[k])
    k=k+1
print(l3)

