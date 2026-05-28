class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        p1 = 0
        p2 = n-1
        flag = True
        while flag is True:
            while s[p1].isalnum() is False:
                p1+=1
                if p1 > n-1:
                    return True
            
            while s[p2].isalnum() is False:
                p2-=1
                if p2<0:
                    return True
            if p1 >= p2:
                return True
            if s[p1].lower() == s[p2].lower():
                p1+=1
                p2-=1
            else:
                print(p1,p2)
                return False
    

        return True
        