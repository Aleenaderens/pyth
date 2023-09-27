# i=0
# k=5
# for i in range (0,5):
#     for j in range(0,-1+5):
#       print("*",end="   ")
#     for j in range (0,k):
#       print(end="   ")
#     k=k-1
#     print()

i=0
k=5
for i in range (0,5):
   for j in range (0,k):
      print(end=" ")
   for j in range (0,-i+5):
       print("*",end=" ")
   k=k+1
   print()