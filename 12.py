#to find the second largest element in the list 

list1 = [15,10,6,999]

large = list1[0]

for num in list1:
    if num>large:
        large = num

second = list1[1]
for num2 in list1:
    if num2<large and num2>second:
        second = num2

print("the second largest number is ",second)

