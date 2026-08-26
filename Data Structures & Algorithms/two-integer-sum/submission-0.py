class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        aset = set()

        for x in nums:

            wanted = target - x
            if wanted in aset:
                return True

        
        return False