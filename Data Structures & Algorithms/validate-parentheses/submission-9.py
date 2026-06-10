class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2==1:
            return False

        m = {'(':')','{':'}','[':']'}
        stack = [0] * (n+1)
        top = 0
        for i in range(n):
            if s[i] not in m.keys():
                if s[i] not in m.values():
                    return False
                else:
                    if stack[top] == 0:
                        return False
                    if m[stack[top]] == s[i]:
                        top-=1
                    else:
                        return False
            else:
                top+=1
                stack[top] = s[i]

            
        if top == 0:
         return True
        return False


        