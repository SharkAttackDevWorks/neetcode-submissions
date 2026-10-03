class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        aset = set(nums)
        best = 0
        for x in nums:
            if x-1 in aset:
                continue
            else:
                count=0
                while x in aset:
                    x+=1
                    count+=1
                best = max(best, count)
        
        return best

