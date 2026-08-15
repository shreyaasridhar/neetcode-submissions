# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tempNode = TreeNode()
        def invertProcess(root):
            if root.left:
                invertProcess(root.left)
            if root.right:
                invertProcess(root.right)
            
            tempNode = root.left
            root.left = root.right
            root.right = tempNode
            return root
            
        if root:
            return invertProcess(root)
        return root