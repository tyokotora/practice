#coding:utf-8

class Queue:
    
    def __init__(self):
        self.items = []

    def is_empty(seif):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

a_queue = Queue()

for i in range(5):
    a_queue.enqueue(i)

while a_queue.size():
    print(a_queue.dequeue())

    
print()
print(a_queue.size())
    
