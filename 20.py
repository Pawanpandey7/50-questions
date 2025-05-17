#rotate a list by k elements 
#method 1
k = int(input("by how much you want to rotate"))
list1 = [1,2,3,4,5]
list2 =[]
for i in range(0,len(list1)):
    list2.append(list1[i-k])

print(list2)


#method 2 
print("rotating right ")
def rotate_right(lst,k):
    k = k%len(lst)
    return lst[-k:]+lst[:-k]

lst = [1,2,4,5,6,7]    
k=int(input("by whow much you want to rotate right"))
print(lst)
print("rotated right: ",rotate_right(lst,k))

print("rotating left")
def rotate_left(lst,k):
    k = k % len(lst)
    return lst[k:]+lst[:k]

lst = [1,2,3,4,5,6,7,8,9]
k = int(input("enter how much you want to rotate left"))
print("rotated left",rotate_left(lst,k))