class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        MAX, MIN = (1 << 31) - 1, -1 << 31
        while x:
            digit = int(math.fmod(x, 10))
            if (res > MAX // 10 or res == MAX // 10 and digit > MAX % 10) or (res < MIN // 10 or res == MIN // 10 and digit < MIN % 10):
                return 0
            res = res * 10 + digit
            x = int(x / 10)
        
        return res
        