class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        n = len(digits)
        char = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []

        def gen(curr,i):
            if i == n-1:
                digit = int(digits[i])
                for c in char[digit-2]:
                    res.append(curr+c)
                return 
            digit = int(digits[i])
            for c in char[digit-2]:
                gen(curr+c,i+1)
        
        gen("",0)
        return res
            