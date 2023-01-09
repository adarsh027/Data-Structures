class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data=data
            return self.data
        if self.data==data:
            return
        if data < self.data:
            if self.left is None:
                self.left = BSTNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BSTNode(data)
            else:
                self.right.insert(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data)
        if self.right:
            self.right.inorder_traversal()
    def preorder_traversal(self):
        print(self.data)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.data)
        
        
    def delete(self, val, root):
        if self.data is None:
            return
        if val < self.data:
            if self.left is None:
                print("Not present")
            else:
                self.left = self.left.delete(val,root)
        elif val > self.data:
            if self.right is None:
                print("Not present")
            else:
                self.right = self.right.delete(val,root)
        else:
            if self.left is None:
                temp=self.right
                if val==root:# if you want to delete the root node
                    self.data=temp.data
                    self.left=temp.left
                    self.right=temp.right
                    temp = None
                    return
                self=None
                return temp
            if self.right is None:
                temp=self.left
                if val==root:
                    self.data=temp.data
                    self.left=temp.left
                    self.right=temp.right
                    temp = None
                    return
                self=None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.data =node.data
            self.right= self.right.delete(node.data, root)
        return self
    
    
def count(node):
    if node is None:
        return 0
    return count(node.left) + count(node.right) + 1
                

bst = BSTNode()
lst=[10,6,3,1,6,98,3,7]
for i in lst:
    if i==lst[0]:
        root=bst.insert(i)
    else:
        bst.insert(i)
  
print(root)
print(count(bst))
if count(bst)>1:
    bst.delete(10,root)
else:
    print(("Can't perform delete"))




# bst.search('B')
bst.inorder_traversal()
# bst.preorder_traversal()
# bst.postorder_traversal()

