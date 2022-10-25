class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Insert method to create nodes
   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
         else:
            self.data = data
# findval method to compare the value with nodes
   def deletion(self,lkpval):
      if lkpval < self.data:
         if self.left is None:
            return str(lkpval)+" Not Found"
         return self.left.deletion(lkpval)
      elif lkpval > self.data:
            if self.right is None:
               return str(lkpval)+" Not Found"
            return self.right.deletion(lkpval)
      else:
            if self.left is None and self.right is not None:
               self.data=self.right.data
               self.right.data=None
               return
            elif self.left is not None:
               self.data=self.left.data
               self.left.data=None
               return
            else:
               self.data=None
               return      
# Print the tree
   def PrintTree(self):
      if self.data is not None:
         if self.left:
            self.left.PrintTree()
         print( self.data)
         if self.right:
            self.right.PrintTree()
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.deletion(12))
root.PrintTree()