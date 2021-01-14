class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None


    def isempty(self):
        if self.head==None:
            return True
        else:
            return False

    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode


    def pop(self):
        if self.isempty():
            return None
        else:
            # remove the head node and make proceeding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        itr = self.head
        if self.isempty():
            print("stack underflow")
        else:
            while itr != None:
                print(itr.data,"-->",end=" ")
                itr = itr.next
            return

mystack = Stack()
mystack.push(11)
mystack.push(22)
mystack.push(33)
mystack.push(44)
mystack.display()
print("\nTop element : ",mystack.peek())
mystack.pop()
mystack.pop()
mystack.display()