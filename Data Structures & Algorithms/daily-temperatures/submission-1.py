class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [(temperatures[0],0)]
        res = [0]*n
        for i in range(1,n):
            while stack and stack[-1][0] < temperatures[i]:
                res[stack[-1][1]] = i-stack[-1][1]
                stack.pop()
            stack.append((temperatures[i],i))

        return res






        