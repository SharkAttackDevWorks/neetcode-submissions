class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        l = 0

        longest = 1

        if len(s) <2 : return len(s)


        for r in range(1,len(s)):

            if len(set(s[l:r+1])) == r-l+1:
                longest = max(longest, r-l+1)

            else:
                while len(set(s[l:r+1])) < r-l+1 and l < r:
                    l+=1

        
        return longest


            

