class Stack:
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        if self.item:
            return self.item.pop()
        else:
            print("stack is empty")

    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            print("stack is empty")
        

    def size(self):
        return len(self.item)

    def isempty(self):
        return len(self.item)==0 

stack = Stack()

stack.push('A')
stack.push('B')
stack.peek()
stack.size()
stack.isempty()
stack.pop()



