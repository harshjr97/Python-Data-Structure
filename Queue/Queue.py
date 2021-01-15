class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return
        return False

    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ("No elements in Queue")

    def size(self):
        return len(self.queue)

    def isempty(self):
        return len(self.queue)==0

    def display(self):
        print(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()
q.dequeue()
q.display()
print(q.size())
print(q.isempty())