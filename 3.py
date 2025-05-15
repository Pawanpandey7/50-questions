# factorial of a number

class FactNum:

    def __init__(self):
        num = int(input("enter the number "))
        f = 1
        for i in range(num,1,-1):
            f=f*i

        print(f" the factorial of {num} is {f}")

obj = FactNum()        
