__author__ = 'daming'

import bst_utils

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


trees= bst_utils.get_test_bsts('sample_bst')

# bst_utils.bst_in_order(trees[1])
bst_utils.disp_bst(trees[1])

bst_utils.disp_bst(trees[0])

obj = Solution()
print obj.isSameTree(trees[1], trees[0])

