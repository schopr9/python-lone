class Node(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    
    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True
    
    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left_child:
                return self.left_child.find(data)
            else:
                return False 
        else:
            if self.right_child:
                return self.right_child.find(data)
            else:
                return False       
    
    def inorder(self):
        if self:
            print str(self.value)
            if self.left_child:
                return self.left_child.inorder()
            if self.right_child:
                return self.right_child.inorder()    
        

class BinarySearchTree(object):
    def __init__():
        self.root = None

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return True            
    
    def find(self, value):
        if self.root:
            return self.root.find(value)
        else:
            return False

    def inorder(self):
        return self.root.inorder()