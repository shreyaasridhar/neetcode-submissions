# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def letsTraverse(root, output):
            print(root.val)
            if root.left:
                letsTraverse(root.left, output)
            output.append(root.val)
            if root.right:
                letsTraverse(root.right, output)
            
            
            return


        if root:
            letsTraverse(root, output)
        return output
