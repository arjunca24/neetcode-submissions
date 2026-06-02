class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        cum = []
        acc = 0
        for h in height:
            acc+=h
            cum.append(acc)

        highest = max(height)
        res = 0
        l = [0,height[0]]
        #r = [1,height[1]]
        for i in range(1,n):
            if height[i] >= l[1]:
                diff = cum[i-1]-cum[l[0]]
                res += l[1]*(i-l[0]-1)
                res -= diff
                l = [i,height[i]]
                if height[i] == highest:
                    break

        r = [n-1,height[n-1]]
        for i in range(n-2,l[0]-1,-1):
            if height[i] >= r[1]:
                
                diff = cum[r[0]-1]-cum[i]
                res += r[1]*(r[0]-i-1)
                res -= diff
                r = [i,height[i]]

        return res
            


            

               
            






            
        