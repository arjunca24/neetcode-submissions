class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        area = 0
        while i < j:
            if heights[i] < heights[j]:
                a = heights[i]*(j-i)
                i+=1
            else:
                a = heights[j]*(j-i)
                j-=1
            if a > area:
                area = a 
        
        return area

        