#print all prime numbers in a range 

for i in range(1,11):
    sum =0
    for j in range(1,i+1):
        if i%j==0:
            sum += 1


    if sum == 2:
        print(i)        
