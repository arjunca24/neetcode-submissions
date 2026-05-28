class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        p1 = 0
        p2 = n-1
        while True:

            if (numbers[p1] + numbers[p2]) > target:
                p2-=1
            elif (numbers[p1] + numbers[p2]) < target:
                p1+=1

            else:
                return [p1+1,p2+1]
            


        