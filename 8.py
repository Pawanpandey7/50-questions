#finding the gcd of the two numbers 


def FindGCD(n1,n2):
    for i in range(n2,0,-1):
        if n1%i==0 and n2%i==0:
            return i

n1 = int(input("enter the first number"))
n2 = int(input("enter the second number"))
print("the gcd of two numbers is ",FindGCD(n1,n2))            

