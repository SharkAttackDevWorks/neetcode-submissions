class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        count1 = Counter(s1)
        if len(s2)<len(s1): return False
        left = 0

        count2 = None
        count2 = Counter(s2[left:len(s1)])
        if count1 == count2:
            return True

        for r in range(len(s1),len(s2)):
            count2[s2[left]]-=1
            left+=1
            count2[s2[r]]+=1
            count2 = +count2
            if count1 == count2:
                return True

        
        return False







        


        