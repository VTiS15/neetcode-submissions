from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = [root.val]
        curr_level = deque([root])
        next_level = []
        while curr_level or next_level:
            while curr_level:
                s = curr_level.popleft()
                # process node s
                if s.left:
                    next_level.append(s.left)
                if s.right:
                    next_level.append(s.right)
            
            if next_level:
                res.append(next_level[-1].val)

            curr_level = deque(next_level)
            next_level = []
        
        return res
        