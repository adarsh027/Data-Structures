class Node:
    def __init__(self, data):
       self.data = data
       self.next = None


class Circular_LL:
    def __init__(self):
        self.head=None
        self.end=None
                
    def print_CLL(self):
        if self.head is None:
            print("CLL is empty")
        else:
            cur_node=self.head
            while cur_node is not None:
                print(cur_node.data)
                if cur_node.next==self.head:# this means cur_node is the last node and you can exit the loop
                    break
                cur_node=cur_node.next
                 
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=Node(data)
            self.head.next= self.head
        else:
          cur_node = self.head
          while cur_node.next != self.head: # reach the last node
              cur_node = cur_node.next
          cur_node.next = new_node
          new_node.next = self.head
        
    def prepend(self, data):
      new_node = Node(data)
      if self.head is None:
          self.head = new_node
      else:
          cur_node = self.head
          while cur_node.next != self.head: #  # reach the last node
              cur_node = cur_node.next
          cur_node.next = new_node
          new_node.next = self.head
          self.head= new_node  

  
#The below portion is yet to be implemented; have just copied it from singly LL pgm for modification in future
    # def insert_after(self,data,x):
    #   if self.head is None:
    #        print("LL is empty")
    #   else:
    #       cur_node = self.head
    #       while cur_node is not None:
    #           if cur_node.data==x:
    #               break
    #           cur_node = cur_node.next
    #       if cur_node is None:
    #           print("not found")
    #       else:
    #           new_node = Node(data)
    #           new_node.next=  cur_node.next
    #           cur_node.next= new_node
          
          
    # def insert_before(self,data,x):
    #   if self.head is None:
    #        print("LL is empty")
    #   else:
    #       cur_node=self.head
    #       while cur_node.next is not None:
    #           if cur_node.next.data==x:
    #               break
    #           cur_node = cur_node.next
    #       if cur_node.next is None:
    #           print("not found")
    #       else:
    #           new_node = Node(data)
    #           if self.head.data==x:
    #               new_node.next= self.head
    #               self.head=  new_node
    #           else:
    #               new_node.next=cur_node.next
    #               cur_node.next =new_node
          


cll= Circular_LL()
cll.append("A")
cll.append("B")
cll.prepend("C")
# cll.append("C")
cll.print_CLL()