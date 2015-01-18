__author__ = 'daming'

import bst_utils

class Solution:
    def preorderTraversalWorkHorse(self, root, result):
        if root:
            result.append(root.val)
            self.preorderTraversalWorkHorse(root.left, result)
            self.preorderTraversalWorkHorse(root.right, result)

    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = []
        self.preorderTraversalWorkHorse(root, result)
        return result

trees= bst_utils.get_test_bsts('sample_bst')
bst_utils.disp_bst(trees[1])

obj = Solution()
print obj.preorderTraversal(trees[1])