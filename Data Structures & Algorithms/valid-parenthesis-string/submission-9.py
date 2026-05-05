from functools import cache


class Solution:
    def checkValidString(self, s: str) -> bool:
        p_stack, s_stack = [], []

        for i, char in enumerate(s):
            if char == "(":
                p_stack.append(i)
            elif char == "*":
                s_stack.append(i)
            else:
                if p_stack:
                    p_stack.pop()
                elif s_stack:
                    s_stack.pop()
                else:
                    return False
        
        while p_stack and s_stack:
            if p_stack.pop() > s_stack.pop():
                return False
        return not p_stack
        