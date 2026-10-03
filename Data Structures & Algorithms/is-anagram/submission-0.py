class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        adic = defaultdict(int)

        for x in s: 
            adic[x] +=1
        
        adic2 = defaultdict(int)

        for x in t:
            adic2[x] +=1
        
        return adic == adic2 