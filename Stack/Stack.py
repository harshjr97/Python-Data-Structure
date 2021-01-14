class Stack:
    def __init__(self):
        self.stack = []


    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isempty(self):
        return len(self.stack)==0

    def size(self):
        return len(self.stack)

    def print(self):
        print(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.print()
print(s.pop())
s.print()
print(s.size())
