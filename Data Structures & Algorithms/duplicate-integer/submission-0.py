class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        aset = set()

        for x in nums:
            if x in aset: return False

            aset.add(x)

        return True