class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        included="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

        included = set(list(included))

        astr=[]

        for x in s:
            if x in included:
                astr.append(x.lower())
        
        print(astr)

        if astr == astr[::-1]:
            return True
        
        return False

