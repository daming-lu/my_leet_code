__author__ = 'daming'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        # cur_node = root
        # if cur_node.left == None and cur_node.right == None:
        #     print cur_node.val
        #     return
        # if root.left != None:
        #     self.__init__(root.left)
        #
        # print root.val
        #
        # if root.right != None:
        #     self.__init__(root.right)
        # self.root = root
        # self.cur_node = root
        # self.stack = []
        # self.goBackFromLeft = False
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.stack) == 0:
            return False
        return True

    # @return an integer, the next smallest number
    def next(self):
        cur_node = self.stack.pop()
        if cur_node.right:
            node = cur_node.right
            while node:
                self.stack.append(node)
                node = node.left
        return cur_node.val



# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

seven   = TreeNode(7)
four    = TreeNode(4)
nine    = TreeNode(9)
three   = TreeNode(3)
five    = TreeNode(5)
eight   = TreeNode(8)
ten     = TreeNode(10)
two     = TreeNode(2)
six     = TreeNode(6)
one     = TreeNode(1)

seven.left = two
two.right = five
five.left = four
four.left = three

# seven.left      = four
# seven.right     = nine
#
# four.left       = three
# four.right      = five
#
# nine.left       = eight
# nine.right      = ten
#
# three.left      = two
#
# five.right      = six
#
# two.left        = one

i, v = BSTIterator(seven), []
while i.hasNext():
    v.append(i.next())

print v