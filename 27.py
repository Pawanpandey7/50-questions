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

#method 2
def quick_sort_in_place(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Pivot is the last element
    i = low - 1        # Index of smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot
    return i + 1

arr = [8, 3, 1, 7, 0, 10, 2]
quick_sort_in_place(arr, 0, len(arr) - 1)
print("Sorted array:", arr)



