import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        largest = []
        for num in nums:
            heapq.heappush_max(largest,num)
            if len(largest) > n-k+1:
                heapq.heappop_max(largest)
        
        return largest[0]

        