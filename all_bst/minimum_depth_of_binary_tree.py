__author__ = 'daming'

class Solution:
    def workhorse(self, cur_node, depth_so_far):
        cur_depth = depth_so_far + 1
        if cur_node.left == None and cur_node.right == None:
            if self.min_depth == -1:
                self.min_depth = cur_depth
            elif cur_depth < self.min_depth:
                self.min_depth = cur_depth
        if cur_node.left:
            self.workhorse(cur_node.left, cur_depth)
        if cur_node.right:
            self.workhorse(cur_node.right, cur_depth)

    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        self.min_depth = -1
        if root == None:
            return 0
        self.workhorse(root, 0)
        return self.min_depth
