__author__ = 'daming'

import bst_utils

class Solution:
    def workhorse(self, cur_node, cur_sum, target_sum):
        if self.found:
            return
        if not cur_node.left and not cur_node.right:
            final_sum = cur_node.val + cur_sum
            if target_sum == final_sum:
                self.found = True
            return
        sum_at_this_node = cur_node.val + cur_sum
        if cur_node.left:
            self.workhorse(cur_node.left, sum_at_this_node, target_sum)
        if cur_node.right:
            self.workhorse(cur_node.right, sum_at_this_node, target_sum)

    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        self.found = False
        if not root:
            return False
        self.workhorse(root, 0, sum)
        return self.found

trees= bst_utils.get_test_bsts('sample_bst')
bst_utils.disp_bst(trees[0])


obj = Solution()
print obj.hasPathSum(trees[0], 114)


# Python list pass by reference
# def test(list1, i):
#     if i>0:
#         list1.append(i)
#         test(list1, i-1)
#
# test1 = []
# for i in range(0,3):
#     test(test1, i)
#
# print test1
