#implementing queue using list
class Queue:
    def __init__(self):
        self.queue = []

    def push(self,item):
        self.queue.append(item)
        print(f"{item } is pushed")

    def pop(self):
        if not len(self.queue) == 0:
            popped = self.queue.pop(0)
            print(f"{popped} is popped") 
            return popped

        else:
            print("queue is empty") 
            return None     

    def peek(self):
        if not len(self.queue) == 0:
            print(self.queue[0])

        else:
            print("queue is empty")   
            return None 

    def Display(self):
        if not len(self.queue) == 0:
            print(self.queue)

        else:
            print("queue is empty")   

             


#creating object 
obj = Queue()
obj.push(2)
obj.push(3)
obj.pop()
obj.peek()
obj.Display()