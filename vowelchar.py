str=input("Enter a word:")
count=0
d={}
for char in str:
    if char.lower() in 'aeiou':
       d[char]=count
    count= count+1 
print(d) 