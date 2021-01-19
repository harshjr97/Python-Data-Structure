class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# insert method to add data in Tree
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


# findval method to compare the value with node
    def findval(self,lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)

        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)

        else:
            return str(self.data)+" is Found"


# In-order Traversal
# left -> root -> right
    def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)
        return res


# Pre-order Traversal
# root -> left -> right
    def preorder(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res


# Post-order Traversal
# left -> right -> root
    def postorder(self, root):
        res = []
        if root:
            res = self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.data)
        return res


    # find max
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # find min
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


# Print Tree Method
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

if __name__ == '__main__':
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    root.printTree()
    print(f"Minimum Value in Tree : {root.find_min()}")
    print(f"Maximum Value in Tree : {root.find_max()}")
    print(f"Inorder : {root.inorder(root)}")
    print(f"Preorder : {root.preorder(root)}")
    print(f"Postorder : {root.postorder(root)}")
    print(root.findval(14))