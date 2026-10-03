class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        aset = set()

        for x in nums:
            if x in aset: return True

            aset.add(x)

        return True