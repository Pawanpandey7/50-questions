#to reverse a string

name = "pawan"
rev_name = ""

n = len(name)
for i in range(n-1,-1,-1):
    rev_name += name[i]

print(rev_name)

name = rev_name[::-1]
print(name)