# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque()

        q.append(root)
        while q:
            level = []
            while q:
                node = q.popleft()
                if node:
                    level.append(node)
            for node in level:
                q.append(node.left)
                q.append(node.right)
            if level:
                res.append([node.val for node in level if node])
        
        return res
        