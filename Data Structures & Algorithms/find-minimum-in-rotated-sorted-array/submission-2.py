class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] < nums[n-1]:
            return nums[0]

        l = 0
        r = n-1
        val = nums[0]
        while r>l:
            d = (l+r)//2
            if nums[d] > val:
                l = d
                val = nums[d]
            else:   
                r = d
        print(l,r)
        return nums[r+1]


        