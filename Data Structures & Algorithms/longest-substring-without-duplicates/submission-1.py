class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        left = 0 
        
        aset = set()

        amax = 0

        for right in range(len(s)):

            while s[right] in aset:
                aset.remove(s[left])
                left+=1

            aset.add(s[right])

            amax = max(amax, len(aset))
        
        return amax
            




