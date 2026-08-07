class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def gen(curr,used):
            nonlocal res
            
            if len(curr) == n:
                    #print(curr,"hi",res)
                    res.append(curr[:])
                    return
            for i in range(n):
                
                if used[i] == 0:
                    curr.append(nums[i])
                    used[i] = 1
                    gen(curr,used)
                    curr.pop()
                    used[i] = 0
                    print(curr,used)
                

        
        gen([],[False]*n)
        return res