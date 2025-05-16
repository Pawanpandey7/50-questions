# sort a list without using sort()
#i will sort the list in ascending order

def bubble_sort(list1):
    n = len(list1)
    for i in range(n):
        for j in range(0,n-i-1):
            if list1[j]>list1[j+1]:
                list1[j+1],list1[j]=list1[j],list1[j+1]



list1=[5,2,7,4,9]
bubble_sort(list1)
print(list1)


