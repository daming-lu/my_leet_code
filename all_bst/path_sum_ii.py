__author__ = 'daming'

import bst_utils

class Solution:
    def workhorse(self, cur_node, cur_sum, list_so_far, target_sum):
        list_so_far.append(cur_node.val)
        if not cur_node.left and not cur_node.right:
            final_sum = cur_node.val + cur_sum
            if target_sum == final_sum:
                self.ans.append(list(list_so_far))
            list_so_far.pop()
            return
        sum_at_this_node = cur_node.val + cur_sum
        if cur_node.left:
            self.workhorse(cur_node.left, sum_at_this_node, list_so_far, target_sum)
        if cur_node.right:
            self.workhorse(cur_node.right, sum_at_this_node, list_so_far, target_sum)
        list_so_far.pop()

    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def pathSum(self, root, sum):
        if root == None:
            return []
        self.ans = []
        self.workhorse(root, 0, [], sum)
        return self.ans

trees= bst_utils.get_test_bsts('sample_bst')
bst_utils.disp_bst(trees[0])


obj = Solution()
print obj.pathSum(trees[0], 22)

"""
# Python list pass by reference
def test(list1, i):
    if i>0:
        list2 = list(list1)
        list2.append(i)
        test(list2, i-1)

test1 = []
for i in range(0,3):
    test(test1, i)

print test1
"""