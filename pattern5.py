i=0
k=5
for i in range (0,5):
   for j in range(0,k):
      print(end="  ")
   for j in range (0,i+1):
      print("*",end="   ")
   k=k-1
   print()
