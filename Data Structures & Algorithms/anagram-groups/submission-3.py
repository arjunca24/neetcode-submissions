class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def checkIsAnagram(a,b):
            
            count1 = {}
            count2 = {}
            if len(a) != len(b):
                return False
            
            for i in range(len(a)):
                count1[a[i]] = 1 + count1.get(a[i],0)
                count2[b[i]] = 1 + count2.get(b[i],0)
            return count1 == count2
        
        group = []
        
        for i in range(len(strs)):
            flag = False
            for j in range(len(group)):
                if (checkIsAnagram(group[j][0],strs[i])):
                    group[j].append(strs[i])
                    flag = True
            if flag == False:
                group.append([strs[i]])

        return group
                