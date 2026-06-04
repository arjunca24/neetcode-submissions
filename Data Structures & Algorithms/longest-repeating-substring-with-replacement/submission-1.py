import heapq
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0
        res = 0
        freq = {}
        h = 0
        

        while r<n:
            print(res)
            freq[s[r]] = 1 + freq.get(s[r],0)
            while (r-l+1) - max(freq.values()) > k:
                freq[s[l]] -=1
                l+=1

            res = max(res,r-l+1)
            r+=1
        
        
        return res
            



            
            
        
        return res





        
        
           


        