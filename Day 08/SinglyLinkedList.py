class Node:
    def __init__(self,value):
        self.value = value
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        
        self.length+=1
        return self
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next
        print("None")

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node

        else:
            new_node.next=self.head
            self.head=new_node

        self.length+=1

    def delete(self):
        if self.length==0:
            print("List is empty")
            return 
        else:
            self.head=self.head.next
    
s = SinglyLinkedList()
s.append(20)
s.append(30)
s.append(40)
s.prepend(100)
s.delete() 
