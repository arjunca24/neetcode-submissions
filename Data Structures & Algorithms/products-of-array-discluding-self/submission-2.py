class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc = 1
        z = 0
        for num in nums:
           if num != 0: 
            acc*= num
           else:
            z+=1  
        output = []
        if z > 1:
            output = [0 for i in range(len(nums))]
            return output

        for i in range(len(nums)):
            if nums[i] == 0:
                output.append(acc)
            else:
             if z == 1:
                output.append(0)
             else:      
              output.append(int(acc/nums[i]))

        return output
        