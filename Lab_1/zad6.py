

class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        #self.parent = None

    def add_child(self, child):
        self.children.append(child)

    # def remove(self):
    #     if self.parent:
    #         self.parent.children.remove(self)
    #         for child in self.children:
    #             child.parent = self.parent
    #             self.parent.children.append(child)
    #     else:
    #         for child in self.children:
    #             child.parent = None
    #     del self

    def __str__(self):
        return str(self.value)

    # def traverse(self):
    #     print(self.value)
    #     for child in self.children:
    #         child.traverse()

    # def traverse(self, parent_str="Root"):
    #     for child in self.children:
    #         print(f"{child} <- {self}", end="  ")
    #         print("")
    #         child.traverse(str(self))

    def trace(self, path=""):
        if self.value:
            if path:
                print(f"{self.value} <- {path}")
            else:
                print(self.value)
        for child in self.children:
            #child.trace(f"{self.value} <- {path}")
            child.trace(f"{self.value} <- {path}" if path else self.value)

'''
# Tworzenie węzłów
root = TreeNode("ROOT")
child1 = TreeNode("Ch1")
child2 = TreeNode("Ch2")
grandchild11 = TreeNode("G11")
grandchild12 = TreeNode("G12")
grandchild13 = TreeNode("G13")
grandchild21 = TreeNode("G21")
grandchild22 = TreeNode("G22")
great_grandchild111 = TreeNode("GG111")
great_grandchild121 = TreeNode("GG121")
great_grandchild122 = TreeNode("GG122")
great_grandchild123 = TreeNode("GG123")
great_grandchild211 = TreeNode("GG211")
great_grandchild212 = TreeNode("GG212")


# Budowanie struktury drzewa
root.add_child(child1)
root.add_child(child2)

child1.add_child(grandchild11)
child1.add_child(grandchild12)
child1.add_child(grandchild13)

child2.add_child(grandchild21)
child2.add_child(grandchild22)

grandchild11.add_child(great_grandchild111)

grandchild12.add_child(great_grandchild121)
grandchild12.add_child(great_grandchild122)
grandchild12.add_child(great_grandchild123)

grandchild21.add_child(great_grandchild211)
grandchild21.add_child(great_grandchild212)

# Wyświetlenie drzewa
root.trace()

# Usuwanie węzła
# child2.remove()
#
# print("\n\t Po Usunieciu: \n")
# root.trace()

'''
