# Implement a FIFO with two LIFO.

class Stack:
    def __init__(self):
       self.content = []
    def pop(self):
        if not self.content:
            return None
        else:
            return self.content.pop()
    def add(self, x):
        self.content.append(x)
    def isVoid(self):
        return not self.content
    def length(self):
        return len(self.content)

class Queue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    def enqueue(self, x):
        if self.stack2.isVoid:
            self.stack1.add(x)
        else:
            for _ in range(self.stack2.length()):
                self.stack1.add(self.stack2.pop())
            self.stack1.add(x)
    def dequeue(self):
        if (not self.stack2.isVoid()):
            return self.stack2.pop()
        else:
            for _ in range(self.stack1.length()):
                self.stack2.add(self.stack1.pop())
            return self.stack2.pop()

test1 = Queue()
test1.enqueue(1)
test1.enqueue(2)
test1.enqueue(3)
print(test1.stack1.content)
print(test1.stack2.content)

print(str(test1.dequeue()))
print(test1.stack1.content)
print(test1.stack2.content)


