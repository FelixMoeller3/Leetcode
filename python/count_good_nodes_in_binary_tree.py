# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree_helper import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        goodNodes = [0]
        
        def dfs(root: TreeNode, maxVal: int) -> None:
            curMax = maxVal
            if not root:
                return
            if root.val >= maxVal:
                goodNodes[0] += 1
                curMax = root.val
            dfs(root.left,curMax)
            dfs(root.right,curMax)

        dfs(root,root.val)
        return goodNodes[0]