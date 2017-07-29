#In which your struly implements a stack in python.

class Stack:
    
    def __init__(self):
        self.items = []

    def is_empty(self):             #Tells us if it's empty.
        return self.items == []

    def push(self, item):           #Adds item to top of stack.
        self.items.append(item)

    def pop(self):                  #Removes item from top of stack.
        return self.items.pop()

    def peek(self):                 #Returns value at top of stack.
        return self.items[len(self.items)-1]

    def size(self):                 #even more self-explanatory.
        return len(self.items)


'''
Gotta say, it seems kinda ironic implementing a stack using all these in-built
data structures. Would C be a better language to learn DSs in, I wonder?
'''
