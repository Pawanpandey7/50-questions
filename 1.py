#even or odd checker 

class Checker:
    def Check(self):
        num = int(input("enter the number"))
        if num%2==0:
            print("even")

        else:
            print("odd")


obj = Checker()
obj.Check()


