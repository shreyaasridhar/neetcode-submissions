# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 1)
    def traverse(self, node, height):
        if not node:
            return height - 1
        l = self.traverse(node.left, height + 1)
        r = self.traverse(node.right, height + 1)
        return max(l,r)