# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List,Optional
from tree_helper import TreeNode

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        def bTree(preorder: List[int], inorder:List[int], parent: Optional[TreeNode]) -> None:
            if not inorder:
                return

            if inorder[0] != parent.val:
                parent.left = TreeNode(preorder[1])
                
            k = inorder.index(parent.val)

            if k > 0:
                bTree(preorder[1:k+1],inorder[0:k],parent.left)

            if k >= len(inorder)-1:
                return
            
            
            parent.right = TreeNode(preorder[k+1])
            bTree(preorder[k+1:],inorder[k+1:],parent.right)



        bTree(preorder,inorder,root)

        return root


if __name__ == "__main__":
    sol = Solution()
    preorder = [1,2,3]
    inorder = [3,2,1]
    root = sol.buildTree(preorder,inorder)