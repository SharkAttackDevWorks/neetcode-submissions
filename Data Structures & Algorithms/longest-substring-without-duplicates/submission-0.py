class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        left = 0 
        
        aset = set()

        amax = 0

        for right in range(len(s)):

            while s[right] not in aset:
                aset.add(s[right])
                right+=1

            amax = max(amax, len(aset))
            




