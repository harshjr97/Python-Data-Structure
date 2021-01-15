class Deque:
    # constructor
    def __init__(self):
        self.item = []

    # method to check is deque is empty
    def isempty(self):
        return self.item == []

    # method to add data in front
    def addfront(self,data):
        self.item.append(data)

    # method to add data in rear
    def addrear(self,data):
        self.item.insert(0,data)

    # method to remove data from front
    def removefront(self):
        return self.item.pop()

    # method to remove data from rear
    def removerear(self):
        return self.item.pop(0)

    # method to get the size of queue
    def size(self):
        return len(self.item)

    # utility function to print deque
    def display(self):
        print(self.item)


if __name__ == '__main__':
    dq = Deque()
    dq.addfront(11)
    dq.addfront(22)
    dq.addfront(33)
    dq.display()
    dq.addrear(99)
    dq.addrear(88)
    dq.display()