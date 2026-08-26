class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        adic = {}

        aset = set(nums)


        longest = 0

        for x in aset:
            if x-1 not in aset:
                alen = 1

                while x + alen in aset:
                    alen+=1

                longest = max(longest, alen)
        
        return longest