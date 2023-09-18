x=input("Enter a word:")
d={}
i=0
while (i<len(x)):
    if x[i] in d:
      d[x[i]]+=1
    else:
        d[x[i]]=1
    i=i+1
print(d)
