class Queue:
    def __init__(self,size):
        self.items=[]
        self.size=size

    def display(self):
        print(self.items)

    def empty(self):
        if len(self.items)==0:
            return True
        
    def insertFromRear(self,element):
        if self.size==len(self.items):
            print("Queue Overflow")
        else:
            self.items.append(element)

    def insertFromFront(self,element):
        if self.size==len(self.items):
            print("Queue Overflow")
        else:
            self.items.insert(element)

    def romoveFromRear(self):
        if self.items==0:
            self.empty
        else:
            self.items.pop()

    def removeFromFront(self):
        if self.items==0:
            self.empty
        else:
            self.items.pop(0)
        


q=Queue(6)
q.insertFromFront(10)
q.display()
