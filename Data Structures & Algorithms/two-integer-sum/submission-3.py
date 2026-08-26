class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        aset = defaultdict(int)

        for i in range(len(nums)):
            
            wanted = target - nums[i]
            if wanted in aset:
                return [aset[wanted], i]
            aset.add(nums[i])

        
        return False