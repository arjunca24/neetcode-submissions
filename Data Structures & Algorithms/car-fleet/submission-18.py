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
      
        stack = [reaches(t[n-1][0],t[n-1][1])]
        length = 0
        for i in range(n-2,-1,-1):
            time = reaches(t[i][0],t[i][1])
            if  time > stack[length]:
                stack.append(time)
                length+=1
                
        return length+1
                



       


        