class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) -1
        res = [[nums[0]]]
        copy = nums

        def add(val,curr):
            temp = []
            for i in range(len(curr)):
                temp.append(curr[0:i] + [val] + curr[i:len(curr)])
            temp.append(curr+[val])
            return temp

        for i in range(1,n+1):
            new = []
            for j in range(len(res)):
                new += add(nums[i],res[j])
            res = new
        return res
        


        