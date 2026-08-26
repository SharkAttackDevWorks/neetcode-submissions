class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s)-1

        included="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        
        while left < right:

            while s[left] not in included and left < right:
                left+=1
            while s[right] not in included and right > left:
                right-=1

            if s[left].lower() != s[right].lower():
                return False
           
            left+=1
            right-=1
        
        return True
