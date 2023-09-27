n=64
j=1
for i in range(1,5):
    for j in range(n,n+i):
      print(chr(n+i),end=" ")
    j=j+i
    print()