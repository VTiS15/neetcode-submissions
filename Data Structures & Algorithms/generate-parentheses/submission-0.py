class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dp(curr: str = "(", stack = ["("], count: int = n - 1):
            if not stack and count == 0:
                res.append(curr)
                return

            if count > 0:
                dp(curr + "(", stack + ["("], count - 1)
            if stack:
                dp(curr + ")", stack[:-1], count)
        
        dp()
        return res
        