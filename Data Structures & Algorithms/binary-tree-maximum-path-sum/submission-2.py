# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = float("-inf")
        def helper(root):
            nonlocal result

            if not root:
                return 0
            
            left_sum = helper(root.left)
            right_sum = helper(root.right)
            path_sum = max(
                left_sum + root.val,
                right_sum + root.val,
                root.val
            )
            candidate_sum = max(path_sum, left_sum + right_sum + root.val)
            result = max(result, candidate_sum)

            return path_sum
        helper(root)
        return result
        # best = float('-inf')
        # def dfs(node):
        #     nonlocal best
        #     if not node:
        #         return 0
        #     left = max(0, dfs(node.left))
        #     right = max(0, dfs(node.right))
        #     best = max(best, node.val + left + right)
        #     return node.val + max(left, right)
        # dfs(root)
        # return best
            