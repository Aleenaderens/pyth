n=63
i=0
j=1
for i in range(0,6):
    for j in range(j,i+j):
      print(chr(j+n),end=" ")
    j=j+1
    print()