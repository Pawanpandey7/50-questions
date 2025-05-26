# two sum problem
def two_sum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i != j and (target - arr[i]) == arr[j]:
                return i, j

arr = [1, 2, 3, 4, 5]
target = 6
print(two_sum(arr, target))  


