class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def reaches(pos, speed):
            return (target-pos)/speed 

        n = len(position)
        if n==1:
            return 1
        t = []
        for i in range(n):
            t.append((position[i],speed[i]))
        t.sort()
        res = 0
        count = 0
        longest = reaches(t[n-1][0],t[n-1][1])
        for i in range(n-1,0,-1):
            print(longest)
            if count == 0:
                res +=1
            if longest >= reaches(t[i-1][0],t[i-1][1]):
                count+=1
            else:
                count = 0
                longest = reaches(t[i-1][0],t[i-1][1])
                if i-1 == 0:
                    res+=1

        
                
                
        return res
                



       


        