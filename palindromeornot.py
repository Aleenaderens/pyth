sen=(input("enter a word:"))
rev=reversed(sen)
if list(sen)==list(rev):
    print("PALINDROME!")
else:
    print("NOT A PALINDROME!")
