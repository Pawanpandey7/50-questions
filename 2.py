# in this program i am checking if the given number is prime or not 

class PrimeChecker:
    def __init__(self,num):
        self.num = num
        self.sum = 0

    def pCheck(self):
        for i in range(1,self.num):
            if self.num%i==0:
                self.sum += 1

        if self.sum>2:
            print("it is a composite number")

        else:
            print("it is a prime number")                 

obj = PrimeChecker(5)
obj.pCheck()
