class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s) -1
        if n == 0:
            return [[s[0]]]
        res = []
        
        def isPalindrome(val):
            m = len(val)
            for i in range(m):
                if val[i] != val[m-i-1]:
                    return False
            return True 

        def split(curr,i):
            if i == n:
                m = len(curr)
                for j in range(m-1):
                    if not isPalindrome(curr[j]):
                        return
                if isPalindrome(curr[m-1]):    
                    res.append(curr+[s[i]])

                last = curr[-1]
                last+=s[i]
                if isPalindrome(last):
                    curr.pop()
                    curr.append(last)
                    res.append(curr)
                return 
            if isPalindrome(curr[-1]):
             split(curr+[s[i]],i+1)
            last = curr.pop()
            last += s[i]
            curr.append(last)
            split(curr,i+1)
        
        split([s[0]],1)
        return res

            
