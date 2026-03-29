 # -----STACK-----

class Stack:
    def __init__(self,size):
        self.stack=[]
        self.size=size

    def push(self, element):
        if self.size==len(self.stack):
            print("Stack Overflow")
        else:
            self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            self.stack.pop()

    def display(self):
        print(self.stack, "Current Stack")

    def peak_element(self):
        if len(self.stack)==0:
            print("Stack is Empty")
        else:
            print(self.stack[-1])


    def isEmpty(self):
        if len(self.stack) == 0:
            return True


s=Stack(6)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.pop()
s.peak_element()
s.display()

