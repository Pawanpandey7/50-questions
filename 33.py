# sum of the array elements usng recursion
def sum_of_array(arr,n):
    if n == 0 :
        return 0

    return arr[n-1] + sum_of_array(arr,n-1)


arr = [1,2,3,4,5]
n = len(arr)
print(sum_of_array(arr,n))
