import _collections_abc
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  
        n = len(matrix)
        m = len(matrix[0])

        def convert(i):
            row = i//m
            col = i%m
            return row,col

        l = 0
        r = n*m -1
        while True:
            d = (r+l) // 2   
            row,col = convert(d)
            val = matrix[row][col]
            if val == target:
                return True
            if val < target:
                l = d+1
            if val > target:
                r = d-1
            if l > r:
                return False

        
            
