# Node class
class Node:
    # func to initialise the node
    def __init__(self,data):
        self.data = data
        self.next = None
        

# Linked list class contains a Node object
class Linkedlist:
    def __init__(self):
        self.head = None
        
    # func to insert a new node at beginning
    def push(self,new_data):
        # allocate node & put in the data
        # make next of new node as head
        # move the head to point to new node
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    # func to insert new node after the given node
    def insertat(self,midnode,newdata):
        if midnode is None:
            print("the mentioned node is absent")
            return

        newnode = Node(newdata)
        newnode.next = midnode.next
        midnode.next = newnode


        
    # func to add new data in end 
    def append(self,new_data):
        # create new node put in the data , set next as none
        new_node = Node(new_data)
        
        # if linked list is empty then make the new node as head
        if self.head is None:
            self.head = new_node
            return
        
        # else traverse till the last node
        last = self.head
        while last.next:
            last = last.next
        # change the next of last node
        last.next = new_node
        
    def getlength(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
        
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,'-->',end=" ")
            temp = temp.next
            
    def deletenode(self,index):
        if index < 0 or index >= self.getlength():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
            
            
if __name__ == '__main__':
    ll=Linkedlist()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    ll.push(7)
    ll.printlist()
    ll.insertat(ll.head.next.next,3)
    print("\n")
    ll.printlist()