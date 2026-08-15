# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(root, depth, maxDepth):
            currDepth = depth + 1
            maxDepth = currDepth if currDepth > maxDepth else maxDepth
            if root.left:
                leftDepth = traverse(root.left, currDepth, maxDepth)
                maxDepth = leftDepth if leftDepth > maxDepth else maxDepth
            if root.right:
                rightDepth = traverse(root.right, currDepth, maxDepth)
                maxDepth = rightDepth if rightDepth > maxDepth else maxDepth
            return maxDepth
        return traverse(root, 0, 0) if root else 0