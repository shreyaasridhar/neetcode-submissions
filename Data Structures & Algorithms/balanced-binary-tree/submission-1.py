# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def checkHeight(node):
            if not node:
                return True, 0
            
            leftBalanced, leftHeight = checkHeight(node.left)
            rightBalanced, rightHeight = checkHeight(node.right)

            isBalanced = leftBalanced and rightBalanced and (abs(leftHeight - rightHeight) <= 1)

            height = 1 + max(leftHeight, rightHeight)
            
            return isBalanced, height

        res, val = checkHeight(root)
        
        return res

        
        