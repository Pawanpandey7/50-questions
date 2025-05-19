#bubble sort:

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]

arr= [2,5,1,7,5,8]                
bubble_sort(arr)
print(arr)

