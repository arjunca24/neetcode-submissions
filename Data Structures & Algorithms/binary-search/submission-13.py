class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        d = int(n/2)
        u = n
        l = 0
        while True:
            d = int((u+l)/2)
            if d > n-1:
                return -1
            if nums[d] == target:
                return d
            elif nums[d] > target:
                u = d-1
            elif nums[d] < target:
                l = d+1
            if l > u:
                return -1
            
        
     
        