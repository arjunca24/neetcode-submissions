class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums2 = set(nums)
        seen = set()
        highest = 0
        for num in nums:
            if num in seen:
                continue
            count = 1 
            over = False
            while over is False:
                if (num+count) in nums2:
                        count+=1
                        seen.add(num+count)
                else:
                    over = True
                    if count > highest:
                        highest = count
        return highest


        