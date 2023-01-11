# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_helper import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            first = p
            second = q
        else:
            second = p
            first = q

        if root.val <= first.val:
            if root.val >= second.val:
                return root
            return self.lowestCommonAncestor(root.right,p,q)
        if root.val <= second.val:
            return root
        return self.lowestCommonAncestor(root.left,p,q)