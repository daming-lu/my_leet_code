
import fileinput
from sys import stdin
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insertNode(root, curNode):
    if root.left is None and root.right is None:
        # leaf node
        if curNode.val >= root.val:
            root.right = curNode
        else:
            root.left = curNode
        return

    if curNode.val >= root.val:
        if root.right is None:
            root.right = curNode
            return
        insertNode(root.right, curNode)
    else:
        if root.left is None:
            root.left = curNode
            return
        insertNode(root.left, curNode)


def buildBST():
    total = -1
    count = 0
    root = None
    for line in fileinput.input():
        if total == -1:
            total = int(line.strip().rstrip())
            continue
        else:
            if count < total:
                curLine = line.strip().rstrip()
                if len(curLine) == 0:
                    continue
                curNode = TreeNode(int(curLine))
                if root is None:
                    root = curNode
                else:
                    insertNode(root, curNode)
                count += 1

    return root


def inOrderDispTree(root):
    if root is None:
        return

    inOrderDispTree(root.left)
    print root.val
    inOrderDispTree(root.right)

def getHeight(root):
    if root is None:
        return 0
        
    left = getHeight(root.left)
    right = getHeight(root.right)
    
    if left == -1 or right == -1:
        return -1 # -1 means not balanced

    if abs(left-right)>1:
        return -1
    
    return max(left, right)+1


def isBalance(root):
    if root is None:
        return True
    if getHeight(root) == -1:
        return False
    return True
    

root1 = buildBST()
inOrderDispTree(root1)

print isBalance(root1)



"""


    15
 8      35
3 13   25 55
            199
           88
"""
