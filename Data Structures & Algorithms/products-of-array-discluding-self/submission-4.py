class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        for i in range(1,n):
            output[i] = output[i-1]*nums[i-1]

        output2 = [1]*n
        for i in range(n-2,-1,-1):
            output2[i] =  output2[i+1]*nums[i+1]
        res = []
        for i in range(n):
            res.append(output[i]*output2[i])
        return res
        