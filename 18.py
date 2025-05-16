# to check if the string is palindrome
# first i need to reverse the string

def is_palindrome(str):
    rev_str = str[::-1]
    if str == rev_str:
        print("it is palindrome")

    else:
        print("it is not palindrome")  

is_palindrome("dodod")          