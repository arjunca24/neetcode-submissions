class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        

        def solve(tar,curr):
            nonlocal res
            if tar == 0:
                curr.sort()
                if curr not in res:
                 res +=[curr]
                return
            for num in nums:
                if num <= tar:
                    solve(tar-num,curr+[num])

        solve(target,[])

        
        return res