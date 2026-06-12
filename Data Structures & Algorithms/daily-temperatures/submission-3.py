class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [(temperatures[0],0)]
        top = 0
        res = [0]*n
        for i in range(1,n):
            while stack and stack[-1][0] < temperatures[i]:
                res[stack[top][1]] = i-stack[top][1]
                stack.pop()
                top-=1
            stack.append((temperatures[i],i))
            top+=1

        return res






        