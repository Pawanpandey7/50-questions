#check th palindrome number

num = input("enter the number")

rev_num = num[::-1]

if num==rev_num:
    print ("it is palindrome")

else:
    print("it is not palindrome")    