class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        adic = defaultdict(int)

        for i in range(len(nums)):

            wanted = target - nums[i]

            if wanted in adic:
                return [adic[wanted], i]
            
            adic[nums[i]] = i

            

            
