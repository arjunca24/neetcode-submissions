class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            val = nums[i]
            for ii in range(i+1,n):
                if nums[ii] == val:
                    return val


        