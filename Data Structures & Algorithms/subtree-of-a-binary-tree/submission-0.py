# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node, subnode):
            # Both are None → same tree
            if not node and not subnode:
                return True
            # One is None but not the other → different
            if not node or not subnode:
                return False
            # Values differ → different
            if node.val != subnode.val:
                return False
            # Recursively check left and right subtrees
            return (sameTree(node.left, subnode.left) and 
                    sameTree(node.right, subnode.right))
        
        # Base cases
        if not subRoot:
            return True
        if not root:
            return False
        
        # Check if current trees match, OR check if subRoot is in left/right subtree
        if sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
        

