class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        l = 0

        longest = 0

        if len(s) <2 : return len(s)


        for r in range(1,len(s)):

            if len(set(s[l:r+1])) == r-l:
                longest = max(longest, r-l)

            else:
                while len(set(s[l:r+1])) < r-l and l < r:
                    l+=1

        
        return longest


            

