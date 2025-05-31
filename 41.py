#check if all the characters are unique in the string
def check_unique(str):
    check = len(set(str))
    if check == len(str):
        print("all the characters in the string are unique")

    else:
        print("all the characters in the string is not unique")

str = input("enter the string")
check_unique(str)        