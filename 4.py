#fibonacchi series upto n terms 
def FibNum():
    num = int(input("enter th no of terms"))
    series = []
    n1 = 0
    n2= 1
    series.append(n1)
    series.append(n2)

    for i in range(1,num-1):
        n3 = n1 + n2
        series.append(n3)
        n1 = n2
        n2 = n3

    return series    

print("the fibonacci series is ",*FibNum())
