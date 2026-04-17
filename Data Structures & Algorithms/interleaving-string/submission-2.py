from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)

        @cache
        def dp(x: int = 0, y: int = 0, z: int = 0):
            if z == n3:
                return x == n1 and y == n2
            
            res = False
            if x < n1 and s1[x] == s3[z]:
                res = dp(x + 1, y, z + 1)
            if not res and y < n2 and s2[y] == s3[z]:
                res = dp(x, y + 1, z + 1)
            
            return res

        return dp()
        