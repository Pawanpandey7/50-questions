# program to find duplicates in the array

#function to find all duplicates elements in an array
def find_duplicates(arr):
    seen = set() #set to store unique elements encountered so far
    duplicates = set() #set to store elements that appear more than once
    #loop through each element in the array
    for num in arr:
        if num in seen: #if the number is already in 'seen', its a duplicate
            duplicates.add(num) #add it to the duplicates set

        else:
            seen.add(num)  #if its the first time we are seeing it add it to seen 

    return list(duplicates)   #convert the set of duplicates to a list and return it      

#test example   
arr = [1,2,2,3,4,4,5]   
print(find_duplicates(arr))     