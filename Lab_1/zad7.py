import unittest
from zad6 import TreeNode

import io
from contextlib import redirect_stdout

class TestTreeNode(unittest.TestCase):

    def test_add_child(self):
        root = TreeNode("Root")
        child = TreeNode("Child")
        root.add_child(child)

        self.assertEqual(root.children[0], child)
        self.assertEqual(root.value, "Root")
        self.assertEqual(child.value, "Child")
        self.assertEqual(root.children[0].value, "Child")



    def test_trace(self):
        root = TreeNode("Root")
        child1 = TreeNode("Child1")
        child2 = TreeNode("Child2")
        grandchild11 = TreeNode("G11")
        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild11)

        with io.StringIO() as buf, redirect_stdout(buf):
            root.trace()
            output = buf.getvalue().strip()
        #self.assertEqual(output, "Root\nChild1 <- Root\nChild2 <- Root")
        self.assertEqual(output, "Root\nChild1 <- Root\nG11 <- Child1 <- Root\nChild2 <- Root")

if __name__ == '__main__':
    unittest.main()
