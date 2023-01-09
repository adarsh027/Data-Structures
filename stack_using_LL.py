#Ref:
#https://www.mygreatlearning.com/blog/python-stack/
#https://realpython.com/how-to-implement-python-stack/
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class Stack:
    #Stack with dummy node
    def __init__(self):
        self.head = None
        self.size = 0

    #  For string representation of the stack
    # def __str__(self):
    #     cur_node = self.head
    #     show = ""
    #     while cur_node is not None:
    #         show += str(cur_node.data) + "\n"
    #         cur_node = cur_node.next
    #     return show
    
    def print_LL(self): 
        if self.head is None:
           print("LL is empty")
        else: 
            cur_node= self.head
            while cur_node is not None:
                cur_node = cur_node.next

    # Retrieve the size of the stack
    def getSize(self):
        return self.size

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Retrieve the top item of the stack
    def peek(self):
        if self.isEmpty():
            print("This is an empty stack")
        else:
            return self.head.next.data

    # Push operation 
    def push(self, data): 
      new_node = Node(data)
      if self.head is None:
          self.head = new_node
      else:
        cur_node = self.head
        while cur_node.next is not None:
            self.size += 1
        cur_node.next = new_node
        
    # Pop Operation
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            remove = self.head.next
            self.head.next = self.head.next.next
            self.size -= 1
            return remove.data

stack = Stack()
stack.print_LL()
# n=20
# for i in range(1, 11):
#       stack.push(n)
#       n+=5
# print(f"Stack:\n{stack}")


