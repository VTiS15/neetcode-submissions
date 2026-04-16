# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Make sure p is smaller than q.
        if p.val > q.val:
            p, q = q, p

        # Case 1: If p <= root <= q then root is the LCA.
        if p.val <= root.val <= q.val:
            return root
        # Case 2: If root > q then recurse into left subtree.
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # Case 3: If root < p then recurse into right subree.
        return self.lowestCommonAncestor(root.right, p, q)
        