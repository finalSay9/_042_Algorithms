from py_algorithims.Binary_S_T.Node import Node_a

class  BST:
    def __init__(self):
        self.root = None

        #insert a value
        def insert(self, value):
            if self.root == None:
                self.root == Node_a(value)
            
            else:
                _insert(self.root, value)

        def _insert(self,current,value):
            if value < current.value:
                if current.left == None:
                    current.value == Node_a(value)
                
                else:
                    _insert(current.left, value)
                
            
            else:
                if current.right == None:
                    current.right == Node_a(value)
                else:
                    _insert(current.right, value)

    



