class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        l = 0

        longest = 1
        if len(s) <2 : return len(s)

        aset = set()
        aset.add(s[0])



        for r in range(1,len(s)):

            aset.add(s[r])

            if len(aset) == r-l+1:
                longest = max(longest, r-l+1)

            else:
                while len(set(s[l:r+1])) < r-l+1 and l < r:
                    aset.remove(s[l])
                    l+=1

            aset.add(s[l])


        
        return longest


            

