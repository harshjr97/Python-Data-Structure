class Node:
    # linked list node consist data and next pointer
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    # constructor with front and rear
    def __init__(self):
        self.front = self.rear = None

    # check queue is empty or not
    def isempty(self):
        return self.front == None

    # method to add data
    def enqueue(self,item):
        # creating a node
        temp = Node(item)
        # if rear exist
        if self.rear == None:
            # appending data between front and rear
            self.front = self.rear = temp
            return
        # else rear next points to temp
        self.rear.next = temp
        # then rear is temp
        self.rear = temp

    # method to remove data
    def dequeue(self):
        if self.isempty():
            return
        # store front in temp variable
        temp = self.front
        # temp points to front next
        self.front = temp.next
        if (self.front == None):
            self.rear = None

    def diaplay(self):
        itr = self.front
        while itr!=None:
            print(itr.data,"-->",end=" ")
            itr=itr.next
        return



if __name__ == '__main__':
    q = Queue()
    q.enqueue(11)
    q.enqueue(22)
    q.enqueue(33)
    q.enqueue(44)
    q.diaplay()
    q.dequeue()
    print("\n")
    q.diaplay()