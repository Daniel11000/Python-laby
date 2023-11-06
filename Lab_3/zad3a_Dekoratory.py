# 3. Dekoratory
#   a. wzbogać klasę Tree o dekorator @property do odczytywania najmniejszej
#       wartości w całym drzewie
#   b. Zaimplementuj funkcję do obliczania kolejnych elementów ciągu
#       Fibonacciego w sposób rekurencyjny, zmierz jej czas działania używając
#       biblioteki timeit, następnie użyj dekoratora @lru_cache, i zmierz czas
#       ponownie
#   c. napisz własny dekorator który zapisze na dysku wynik działania funkcji i przy
#       kolejnym użyciu wczyta go z dysku zamiast obliczać ponownie (mogą to być
#       obliczenia na tabeli z poprzedniego zadania)
#   d. * dodaj argument dekoratora decydujący o formacie zapisu (pickle, csv, excel,
#       …)




class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    @property
    def __str__(self):
        return str(self.value)


    def trace(self, path=""):
        if self.value:
            if path:
                print(f"{self.value} <- {path}")
            else:
                print(self.value)
        for child in self.children:
            child.trace(f"{self.value} <- {path}" if path else self.value)


    # --------------------------------------------

    '''
    def min_value(self):
        return self._find_min_value()

    def _find_min_value(self):
        if not self.children:
            return self.value
        min_val = self.value
        for child in self.children:
            min_val = min(min_val, child._find_min_value())
        return min_val
    '''

    # def property(__str__):
    #     def inner_f(self):
    #         if not self.children:
    #             return self.value
    #         min_val = self.value
    #         for child in self.children:
    #             min_val = min(min_val, child._find_min_value())
    #         return min_val
    #     return self.inner_f()


    # def property(func):
    #     def wrapper(self):
    #         if not self.children:
    #             return self.value
    #         min_val = self.value
    #         for child in self.children:
    #             min_val = min(min_val, child._find_min_value())
    #         return min_val
    #     return self.wrapper()


    @property
    def min_value_in_tree(self):
        return self._find_min_value()

    def _find_min_value(self):
        if not self.children:
            return self.value
        min_val = self.value
        for child in self.children:
            min_val = min(min_val, child._find_min_value())
        return min_val

    def __str__(self):
        return f"Node value: {self.value}, Min value in tree: {self.min_value_in_tree}"


# --------------------------

    # def property(func):
    #     def min_value_in_tree(self):
    #         return self._find_min_value()
    #
    #     def _find_min_value(self):
    #         if not self.children:
    #             return self.value
    #         min_val = self.value
    #         for child in self.children:
    #             min_val = min(min_val, child._find_min_value())
    #         return min_val

#'''
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

# Printowanie
print()
print("root: ", root)
print("child2: ", child2)
print("grandchild12: ", grandchild12)

# Usuwanie węzła
# child2.remove()
#
# print("\n\t Po Usunieciu: \n")
# root.trace()

#'''


# --------------- Dekoratory --------------------------

print("--------------------------------------------")
# print(root.min_value())
# print(child2.min_value())
#
# print(child1._find_min_value())


