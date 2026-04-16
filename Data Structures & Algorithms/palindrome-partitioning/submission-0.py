class Solution:
    def is_palindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def recurse(i: int = 0, j: int = 1, entry: list[str] = []):
            if j > n:
                if len("".join(entry)) == n:
                    res.append(entry)
                return

            if self.is_palindrome(s[i:j]):
                recurse(j, j + 1, entry + [s[i:j]])
            recurse(i, j + 1, entry)
        
        recurse()
        return res
        