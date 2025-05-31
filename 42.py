#implementing stack using list
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)  
        print(f"pushed {item}")  

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped: {item}")    
            return item

        else:
            print("Stack is empty. Cannot pop.")  
            return None  

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. Nothing to peek")
            return None            

    def is_empty(self):
        return len(self.stack) == 0


    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack:", self.stack)   



s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
print(s.peek())
s.pop()
s.display()
print(s.is_empty())
print(s.size())
