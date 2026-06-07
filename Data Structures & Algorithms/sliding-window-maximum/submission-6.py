import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        h = []
        for i in range(0,k):
            h.append((-1*nums[i],i))

        heapq.heapify(h)
        res = [h[0][0]*-1]
        for i in range(k,n):

            heapq.heappush(h,(-1*nums[i],i))

            while True:
                curr =  h[0]
                if curr[1] < i-k+1 or curr[1] > i+k-1:
                    heapq.heappop(h)
                else:
                    res.append(-1*curr[0])
                    break    
        return res





        