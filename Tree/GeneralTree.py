class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    def getlevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printtree(self):
        spaces = " " * self.getlevel() * 3
        prefix = spaces + "|-->" if self.parent else ""
        print(prefix + self.data)
        if self.child:
            for child in self.child:
                child.printtree()

    def addchild(self,child):
        child.parent = self
        self.child.append(child)


def buildproducttree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.addchild(TreeNode("MAC"))
    laptop.addchild(TreeNode("Surface"))
    laptop.addchild(TreeNode("ASUS"))

    cellphone = TreeNode("Cell Phone")
    cellphone.addchild(TreeNode("IPhone"))
    cellphone.addchild(TreeNode("Honor"))
    cellphone.addchild(TreeNode("Samsung S20"))

    tv = TreeNode("TV")
    tv.addchild(TreeNode("Sony"))
    tv.addchild(TreeNode("Samsung"))
    tv.addchild(TreeNode("LG"))

    root.addchild(laptop)
    root.addchild(cellphone)
    root.addchild(tv)

    root.printtree()

if __name__ == '__main__':
    buildproducttree()