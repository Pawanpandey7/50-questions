#intesection of two arrays
#1
def intersect_arr(arr1,arr2):
    result = []
    for num in arr1:
        if num in arr2:
            result.append(num)

    return result        


arr1 = [1,2,3,4,5]  
arr2 = [2,3,4]  
print(intersect_arr(arr1,arr2))

#2
def intersect_arr(arr1,arr2):
    return list(set(arr1) & set(arr2))

arr1 = [1,2,3,4,5]
arr2 = [2,3,4]   
print(intersect_arr(arr1,arr2)) 
