__author__ = 'daming'

import bst_utils

class Solution:
    def workhorse(self, cur_node, cur_sum):
        cur_val = cur_sum*10 + int(cur_node.val)
        if not cur_node.left and not cur_node.right:
            self.sum += cur_val
            return
        if cur_node.left:
            self.workhorse(cur_node.left, cur_val)
        if cur_node.right:
            self.workhorse(cur_node.right, cur_val)


    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0
        self.sum = 0
        self.workhorse(root, self.sum)
        return self.sum

trees= bst_utils.get_test_bsts('sample_bst')
bst_utils.disp_bst(trees[0])

obj = Solution()
print obj.sumNumbers(trees[0])