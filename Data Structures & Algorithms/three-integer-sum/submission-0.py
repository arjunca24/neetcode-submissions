class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        vals = {}
        for num in nums:
            vals[num] = 1 + vals.get(num,0)

        def twosum(target):

            combs = set()
            comb = []
            for num in nums:
                rem = target-num
                if rem == (target*-1) and rem == num:
                    if vals[rem] > 2 :
                        comb  = (target*-1,rem,num)
                elif rem == (target*-1):
                   if vals[rem] > 1: 
                    comb  = (target*-1,rem,num)

                elif num == (target*-1):
                   if vals[num] > 1 and rem in nums: 
                    comb  = (target*-1,rem,num)
                elif rem in vals:
                    if rem == num:
                        if vals[rem] > 1:
                            comb  = (target*-1,rem,num)
                    else:
                       comb  = (target*-1,rem,num)
                if len(comb) == 0:
                    continue
                combs.add(tuple(sorted(comb)))
            return combs
        
        comb = set()
        for num in nums:
            combs = twosum(num*-1)
            for val in combs:
                comb.add(val)
        combs = []
        for val in comb:
            combs.append(list(val))    

        return combs




        