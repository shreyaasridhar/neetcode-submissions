# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root):
            left = right = None
            if root.left:
                left = traverse(root.left)
            if root.right:
                right = traverse(root.right)
            root.left = right
            root.right = left
            return root     
        return traverse(root) if root else root