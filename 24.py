#selection sort
#sorting the list in ascending order


def selection_sort(arr):
    n = len(arr)
    current = arr[0]
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

arr = [10,6,8,2,9,4]
selection_sort(arr)
print(arr)


                