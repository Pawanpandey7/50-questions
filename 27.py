#method 1 

def quick_sort(arr):
    if len(arr)<=1:
        return arr # already sorted since there is no elements or 1 element


    pivot = arr[0] 
    left = [x for x in arr[1:] if x < pivot]  
    right = [x for x in arr[1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [8,2,1,7,83,11]
sorted_arr = quick_sort(arr)
print("Sorted array",sorted_arr)



