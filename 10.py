# a program to reverse a number 
# we can reverse a numer in number of ways in python lets go into them

n1 = input("enter the first number")
print("the reverse of the given number is ",n1[::-1])

n2= int(input("enter the second number"))

sum =0

while n2>0:
    sum = (sum*10) + (n2%10)
    n2 //= 10

print("the reverse of this number is ", sum)