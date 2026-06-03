class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        seen = {s[0]}
        l = 0
        r = 1
        highest = 0
        while l<=r and r<n:
            print(l,r)
            print(seen)
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            
            seen.add(s[r])
                
            highest = max(highest,r-l+1)
            r+=1
        
        return highest



            

                



                

        