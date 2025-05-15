#check armstrong number

num = input("enter the number")
check = num
sum = 0
for i in range(0,len(num)):
    inum = int(num[i])
    sum = sum + (inum*inum*inum)

if sum==int(check):
    print("it is armstrong number")

else:
    print("it is not a armstrong number")    
