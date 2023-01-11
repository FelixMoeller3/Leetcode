# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, Tuple
from tree_helper import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def dfs(root: Optional[TreeNode]) -> Tuple[bool,int]:
            if not root:
                return True,-1
            leftBalanced,leftHeight = dfs(root.left)
            rightBalanced,rightHeight = dfs(root.right)
            if not leftBalanced or not rightBalanced:
                return False,-2
            return abs(leftHeight-rightHeight)<=1,1+max(leftHeight,rightHeight)

        return dfs(root)[0]