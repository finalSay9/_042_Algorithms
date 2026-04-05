class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        

class BinarySearchTree():
  
    def __init__(self,root):
        self.node = root


    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else: self._insert_recursive(self.root,key)

    def _insert_recursive(self, current, key):
        if key < current.key:
            if current.left == None:
                current.left = None(key)




       
