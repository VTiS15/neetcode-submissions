class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif stack:
                top = stack.pop()
                if char == ")" and top != "(" or char == "]" and top != "[" or char == "}" and top != "{":
                    return False
            else:
                return False
        return not bool(stack)
        