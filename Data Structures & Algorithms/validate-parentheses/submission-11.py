class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2==1:
            return False

        m = {'(':')','{':'}','[':']'}
        stack = []
        for c in s:
            if c in m.keys(): 
                stack.append(c)
            elif c in m.values():
                if not stack:
                    return False
                if m[stack[-1]] == c:
                    stack.pop()
                else: 
                    return False
        return True if not stack else False



        