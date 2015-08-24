__author__ = 'daminglu'

import bst_utils

from bst_utils import TreeNode

class Solution:
    def find(self, iter, target, path, ans): # can it be a double hit?
        if len(ans) > 0 and ans[-1] == target:
            return
        if iter is None:
            return
        # print iter.val, ', ans : ', ans

        if iter == target:
            path.append(iter)
            ans[:] = list(path)
            print 'Found', ans
            return

        path.append(iter)
        self.find(iter.left, target, path, ans)
        self.find(iter.right, target, path, ans)
        path.pop()
        return

    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        l_p = []
        l_q = []

        self.find(root,p,[],l_p)
        self.find(root,q,[],l_q)
        print l_p
        print l_q
        min_len = min(len(l_p), len(l_q))
        print 'min_len : ', min_len
        for i in range(0, min_len):
            if l_p[i] != l_q[i]:
                return l_p[i-1]
        return l_p[min_len-1]

# tree1 = bst_utils.build_tree([10,7,15,'#',9,14,20])
#
# bst_utils.disp_bst(tree1)
# print tree1.left.right
#
# obj = Solution()
# print obj.lowestCommonAncestor(tree1, tree1.left.right, tree1.right.left)

tree1 = bst_utils.build_tree([-1,0,3,-2,4,'#','#',8])

bst_utils.disp_bst(tree1)

obj = Solution()
ans = obj.lowestCommonAncestor(tree1, tree1.left.left.left, tree1.right)
print 'ans : ', ans
