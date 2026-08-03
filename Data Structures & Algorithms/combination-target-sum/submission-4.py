class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(nums)
        

        def solve(tar,curr,start):
            nonlocal res
            if tar == 0:
                
                res +=[curr]
                return
            for i in range(start,n):
                if nums[i] <= tar:
                    solve(tar-nums[i],curr+[nums[i]],i)

        solve(target,[],0)

        
        return res