class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums2 = set(nums)
        #seen = set()
        highest = 0
        for num in nums2:
            if (num-1) in nums2:
                continue
            count = 1 
            over = False
            while over is False:
                if (num+count) in nums2:
                        count+=1
                        
                else:
                    over = True
                    if count > highest:
                        highest = count
        return highest


        