# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from tree_helper import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodeList = []

        def inOrderTraversal(root: Optional[TreeNode]) -> None:
            if not root:
                return
            inOrderTraversal(root.left)
            nodeList.append(root.val)
            inOrderTraversal(root.right)
        
        inOrderTraversal(root)
        for i in range(1,len(nodeList)):
            if nodeList[i-1] >= nodeList[i]:
                return False

        return True