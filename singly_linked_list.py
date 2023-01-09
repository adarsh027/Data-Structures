#Linked List
# (1) The 1st node of a LL is known as head node. A LL object contains a reference variable, head,
# to store the address of 1st(head) node of LL. When the LL object is created, the reference variable
# head is initialized to None, indicating that the LL is empty.

# (2) Every node in a non-empty LL will have 2 fields:
# a.data : to store the dat of any type(string, integer, float, etc)
# b.next : reference variable that will store the address of next node in the LL.

#(3) To traverse a non-empty LL, you need to start with the head node.

## SLL v/s DLL
## In the case of DLL, if you have the pointer to the node where a new node is to be inserted, then time complexity for insertion is O(1).Otherwise, it is O(n), just like SLL.
## In the case of DLL, if you have the pointer to the node which is to be deleted, then time complexity for deletion is O(1).Otherwise, it is O(n), just like SLL.
## In the case of SLL, you need to know the pointer of previous node of the node(where a new node is to be inserted or which is to be deleted) to achieve the time complexity of O(1)
## Ref: https://cs.stackexchange.com/questions/146260/complexity-of-insertion-into-a-linked-list-single-vs-double
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_LL(self): # Traverse through LL and print all data and count of nodes.
        count=0
        if self.head is None:
           print("LL is empty")
        else: 
            cur_node= self.head
            while cur_node is not None:# when cur_node is None, it means you have already visited all nodes
                print(cur_node.data)
                cur_node = cur_node.next
                count=count+1
        print(count)
        
    def append(self, data): # remember for append, you need to make the next of last node to point to the new node.
      new_node = Node(data)
      if self.head is None:
          self.head = new_node
      else:
        cur_node = self.head
        while cur_node.next is not None: # when cur_node.next is None, it means you are at the last node.
            cur_node = cur_node.next
        cur_node.next = new_node
               
    def prepend(self, data):# remember for prepend, you need to make the head to point to the new node.
      new_node = Node(data)
      if self.head is None:
          self.head = new_node
      else:
          new_node.next = self.head
          self.head= new_node
      
    def insert_after(self,data,x): # reach x
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
              cur_node.next= new_node
          
          
    def insert_before(self,data,x):# reach upto the node before x
      if self.head is None:
           print("LL is empty")
      else:
          cur_node=self.head
          while cur_node.next is not None:
              if cur_node.next.data==x:
                  break
              cur_node = cur_node.next
          if cur_node.next is None:
              print("not found")
          else:
              new_node = Node(data)
              if self.head.data==x:
                  new_node.next= self.head
                  self.head=  new_node
              else:
                  new_node.next=cur_node.next
                  cur_node.next =new_node
          
          
    def insert_by_postion(self,data,pos):
      new_node = Node(data)
      if pos==0:  # if insertion is at the 0th postion, ie, the head node postion
          new_node.next=self.head
          self.head= new_node
          return
          
      cur_node=self.head
      for i in range(pos-1):# reach the previous node of the node at pos
          cur_node=cur_node.next
          
      new_node.next=  cur_node.next
      cur_node.next= new_node
      
           
    def delete_start(self): # delete at start
        if self.head is None:
           print("LL is empty")
        else:
            self.head=self.head.next # settting head to to next node of the current head(1st node)
            

    def delete_end(self): # delete at end
        if self.head is None:
           print("LL is empty")
        elif self.head.next is None: #if LL contains only 1 node
            self.head=None
        else:
            cur_node= self.head
            while cur_node.next.next is not None:# reach second last node
                cur_node=cur_node.next
                
            cur_node.next= None # settting next of second last node to None
            
    def delete(self,x): # delete by value
        if self.head is None:
           print("LL is empty")
           
        elif self.head.data==x:
            self.head=self.head.next
            
        else:
            cur_node = self.head
            while cur_node.next is not None:# reach the node before the x(ie, previous node of x)
                if cur_node.next.data==x:
                    break
                cur_node=cur_node.next
            
            if cur_node.next is None:
                print("not found")
            else:
                cur_node.next=cur_node.next.next # Set the next of previous node of x to the next of x
                


LL= LinkedList()
LL.append("A")
LL.append("B")
LL.append("C")
# LL.append("D")
# LL.append("E")
# # LL.prepend("Z")
# LL.insert_after("Z", "A")
# LL.insert_before("Z", "X")
# LL.insert_by_postion("Z",3)
LL.delete("C")
# LL.delete_start()
# LL.delete_end()
LL.print_LL()

