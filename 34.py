# reverse of the string using recursion
#define a function 'rev_str' that takes a string 'str' and its length 'n'
def rev_str(str,n):

    #base case: if the length is 0, return an empty string(end of recursion)
        
            if n == 0:
                return ""

        #recursive case: take the last character and 
        #concatenate it witht he result of reversing the rest of the string
            return str[n-1]+rev_str(str,n-1)    
            
#declare a string 'str' with the value "pawan"        
str ="pawan"
#get the length of the string and store it in variable 'n'
n = len(str)
#call the function 'rev_str' with the string and its length
#then print the result (which is the reversed string)
print(rev_str(str,n))