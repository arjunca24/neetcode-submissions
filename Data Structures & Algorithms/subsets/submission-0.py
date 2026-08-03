class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)-1
        res = []
        
        def answer(curr,ind):
            if ind == n:
                res.append(curr)
                res.append(curr+[nums[ind]])
                return       
            answer(curr + [nums[ind]],ind+1)
            answer(curr,ind+1)

        i = 0
        answer([],i)
        return res
