#Ref:
#https://www.mygreatlearning.com/blog/python-Queue/
#https://realpython.com/how-to-implement-python-Queue/
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def print_LL(self): 
        if self.head is None:
           print("LL is empty")
        else: 
            cur_node= self.head
            while cur_node is not None:
                print(cur_node.data)
                cur_node = cur_node.next

    # Retrieve the size of the Queue
    def getSize(self):
        return self.size

    # Check if the Queue is empty
    def isEmpty(self):
        return self.size == 0

    # Retrieve the top item of the Queue
    def peek(self):
        if self.isEmpty():
            raise Exception("This is an empty Queue")
        return self.head.next.data

    def enqueue(self, data): 
      new_node = Node(data)
      if self.head is None:
          self.head = new_node
      else:
        cur_node = self.head
        while cur_node.next is not None: 
            cur_node = cur_node.next
            self.size += 1
        cur_node.next = new_node
        
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            remove = self.head.next
            self.head.next = self.head.next.next
            self.size -= 1
            return remove.data

q = Queue()
q.enqueue('A')
q.enqueue('B')
q.dequeue()
q.print_LL()
