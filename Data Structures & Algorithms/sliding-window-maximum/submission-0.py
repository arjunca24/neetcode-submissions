import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        h = []
        for i in range(0,k):
            h.append(-1*nums[i])

        heapq.heapify(h)
        res = [h[0]*-1]
        for i in range(k,n):

            ind = h.index(-1*nums[i-k])
            h[ind] = nums[i]*-1
            heapq.heapify(h)
            res.append(h[0]*-1)
        return res





        