
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def print_LL(self): # Traverse through LL and print all data and count of nodes.
        if self.head is None:
           print("LL is empty")
        else: 
            cur_node= self.head
            while cur_node is not None:# when cur_node is None, it means you have already visited all nodes
                print(cur_node.data)
                cur_node = cur_node.next

        
    def print_LL_reverse(self): # Traverse through LL and print all data and count of nodes.
        if self.head is None:
           print("LL is empty")
        else: 
            cur_node= self.head
            while cur_node.next is not None:# when cur_node.next is None, it means your cur_node is the last node.
                cur_node = cur_node.next
            while cur_node is not None: # as you are at the last node, traverse in  reverse direction
                print(cur_node.data)
                cur_node = cur_node.prev
                
    def append(self, data):
      new_node = Node(data)
      if self.head is None:
          self.head = new_node
      else:
        cur_node = self.head
        while cur_node.next is not None: # when cur_node.next is None, it means you are at the last node.
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.prev = cur_node
               
    def prepend(self, data):
      new_node = Node(data)
      if self.head is None:
          self.head = new_node
      else:
          new_node.next = self.head
          self.head.prev= new_node
          self.head= new_node

    def insert_after(self,data,x): #Remember, for all nodes except the last node, you need set prev of next node of x to new_node
      if self.head is None:
           print("LL is empty")
      else:
          cur_node = self.head
          while cur_node is not None:
              if cur_node.data==x:
                  break
              cur_node = cur_node.next
          if cur_node is None:
              print("not found")
          else:
              new_node = Node(data)
              new_node.next=  cur_node.next
              new_node.prev= cur_node
              if cur_node.next is not None: # if x(cur_node) is not last node, set prev of next node of x to new_node
                  cur_node.next.prev=new_node
              cur_node.next= new_node
                
    def insert_before(self,data,x): #Remember, for all nodes except the 1st(head) node, you need set next of prev node of x to new_node
      if self.head is None:
           print("LL is empty")
      else:
          cur_node=self.head
          while cur_node is not None:
              if cur_node.data==x:
                  break
              cur_node = cur_node.next
          if cur_node is None:
              print("not found")
          else:
              new_node = Node(data)
              new_node.next=  cur_node
              new_node.prev = cur_node.prev
              if cur_node.prev is None: # if x(cur_node) is 1st(head) node, set head to new_node
                  self.head=  new_node
              else:              # if x is not 1st(head) node, set next of previous node of x to new_node
                  cur_node.prev.next= new_node 
              cur_node.prev= new_node
              
    def delete_start(self): # delete at start
        if self.head is None:
           print("LL is empty")
        elif self.head.next is None: #if LL contains only 1 node
            self.head = None
        else:
            self.head=self.head.next
            self.head.prev= None
            
                     
    def delete_end(self): # delete at end
        if self.head is None:
           print("LL is empty")
        elif self.head.next is None: #if LL contains only 1 node
            self.head=None
        else:
            cur_node= self.head
            while cur_node.next is not None:# reach last node(since we are dealing with DLL, we can access second last node from the last node. )
                cur_node=cur_node.next
                
            cur_node.prev.next= None # settting next of second last node to None
            
    def delete(self,x): # delete by value
        if self.head is None:
           print("LL is empty")
           
        elif self.head.data==x:
            self.head=self.head.next
            
        else:
            cur_node = self.head
            while cur_node.next is not None:# reach x
                if cur_node.data==x:
                    break
                cur_node=cur_node.next
            
            if cur_node.next is None:# if you have reached the last node, 2 possibilties
                if cur_node.data==x:     # last node is the x to be deleted
                    cur_node.prev.next= None
                else:                     # this means x is not found in the entire DLL
                    print("not found")
            else:                         # if x is not the last node
                cur_node.next.prev=cur_node.prev #  update prev of next of x  to prev of x
                cur_node.prev.next= cur_node.next#  update next of prev of x to next of x
                
                

dll=DoublyLinkedList()
# dll.print_LL()
# dll.print_LL_reverse()
dll.append('A')
dll.append('B')
dll.append('C')
dll.append('D')
# dll.prepend('Z')
# dll.insert_after('Z','A')
#dll.insert_before('Y','B')
# dll.delete_end()
dll.delete1("D")
dll.print_LL()
