class Btree():
    def __init__(self):
        self.key=None
        self.left=None
        self.right=None
    def insert(self,val,root):
        n=Btree()
        parent=root
        current=root
        n.key=val
        if(root==None):
            root=n
            return root
        else:
            while (current):
                parent = current
                if(val>current.key):
                    current=current.right
                elif(val<current.key):
                    current=current.left
            if(val>parent.key):
                parent.right=n
            else:
                parent.left=n
    def inorder(self,root):
        if root:
            if(root.left):
                self.inorder(root.left)
            print(root.key)
            if(root.right):
                self.inorder(root.right)
root=None
bt=Btree()
root=bt.insert(9,root)
bt.insert(5,root)
bt.insert(13,root)
bt.insert(4,root)
bt.insert(8,root)
bt.insert(10,root)
bt.insert(14,root)
bt.inorder(root)


