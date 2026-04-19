# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min_val = -1001, max_val = 1001):
            if not root:
                return True
            if not min_val < root.val < max_val:
                return False
            return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)
        
        return dfs(root)
        