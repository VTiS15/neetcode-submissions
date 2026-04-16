# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode], depth: int = 0) -> int:
        if not root:
            return depth

        depth += 1

        return max(self.dfs(root.left, depth), self.dfs(root.right, depth))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
        