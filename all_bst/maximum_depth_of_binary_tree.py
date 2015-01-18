__author__ = 'daming'
import bst_utils

class Solution:
    def workhorse(self, cur_node, depth_so_far):
        cur_depth = depth_so_far + 1
        if cur_node.left == None and cur_node.right == None:
            if cur_depth > self.max_depth:
                self.max_depth = cur_depth
        if cur_node.left:
            self.workhorse(cur_node.left, cur_depth)
        if cur_node.right:
            self.workhorse(cur_node.right, cur_depth)


    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        self.max_depth = 0
        if root == None:
            return 0
        self.workhorse(root, 0)
        return self.max_depth