# Ref: https://geekflare.com/python-queue-implementation/

class Queue:
    def __init__(self):
        self.item = []

    def enqueue(self, item):
        # self.item.insert(0,item)
        self.item.append(item)

    def dequeue(self):
        if self.item:
            return self.item.pop(0)
        else:
            print("queue is empty")

    def front(self):
        if self.item:
            return self.item[0]
        else:
            print("queue is empty")
            
    def rear(self):
        if self.item:
            return self.item[-1]
        else:
            print("queue is empty")
        

    def size(self):
        return len(self.item)

    def isempty(self):
        return len(self.item)==0 
    
    def display(self):
        print(self.item)

q = Queue()

q.enqueue('A')
q.enqueue('B')
q.display()
q.peek()
q.size()
q.isempty()
q.dequeue()
