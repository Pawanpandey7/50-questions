#insertion sort
def insertion_sort(arr):
    n =len(arr)
    for i in range(1,n):
        j=i
        while j>0 and arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
                j-=1


arr = [1,8,3,2,0]
insertion_sort(arr)
print(arr)