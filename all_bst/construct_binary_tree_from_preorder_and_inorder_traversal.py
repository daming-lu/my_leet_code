__author__ = 'daming'

import bst_utils

from bst_utils import TreeNode

class Solution:

    def workhorse(self, preorder_orig, preorder_start, preorder_end,
                        inorder_orig,  inorder_start,  inorder_end):
        # print 'pre : ', preorder_orig[preorder_start: preorder_end]
        # print 'in  : ', inorder_orig[inorder_start: inorder_end]
        if preorder_end == preorder_start:
            # print 'create leaf None'
            return None
        if preorder_end == preorder_start + 1:
            # print 'create leaf node : ',preorder_orig[preorder_start]
            return TreeNode(preorder_orig[preorder_start])

        # print preorder, " : ", preorder_start
        cur_node_val = preorder_orig[preorder_start]
        # print 'cur_root ', cur_node_val
        pos_in_inorder = [i for i, x in enumerate(inorder_orig) if x == cur_node_val]
        pos_in_inorder = pos_in_inorder[0]

        cur_node = TreeNode(cur_node_val)

        cur_node.left = self.workhorse(preorder_orig,
                                       preorder_start+1, preorder_start+pos_in_inorder-inorder_start+1,
                                       inorder_orig,
                                       inorder_start, inorder_start+pos_in_inorder)

        cur_node.right = self.workhorse(preorder_orig,
                                        preorder_start+pos_in_inorder-inorder_start+1, preorder_end,
                                        inorder_orig,
                                        pos_in_inorder+1, inorder_end)

        return cur_node

    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if preorder == None or inorder == None:
            return None
        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])

        return self.workhorse(preorder, 0, len(preorder), inorder, 0, len(inorder))

obj = Solution()

preorder = [1,2]
inorder  = [2,1]

root = obj.buildTree(preorder,inorder)
bst_utils.disp_bst(root)

