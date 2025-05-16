#frequency count of characters in the string
str="hello world"
frq= {}

for char in str:
    if char in frq:
        frq[char]+=1

    else:
        frq[char]=1


print(frq)    





