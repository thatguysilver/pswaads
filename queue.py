#We make a queue.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        'Adds to beginning of queue.'
        self.items.insert(0, item)
    
    def dequeue(self):
        'Removes item from end of queue.'
        return self.items.pop()
    
    def is_empty(self):
        
        return self.items == []
        
    def size(self):
        return len(self.items)


a = Queue()
a.enqueue('adam')

print(a.items)
