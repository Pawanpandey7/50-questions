#binary search
import math
def binary_search(arr,start,end,target):
    middle = math.floor((start+end)/2)
    if arr[middle]==target:
        return middle


    elif arr[middle]<target:
        return binary_search(arr,middle,end,target)

    else:
        return binary_search(arr,start,middle,target)


arr = [1,2,3,4,5,6]     
target = 4
start = 0
end = len(arr)
print(binary_search(arr,start,end,target))      
            


