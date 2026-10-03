class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        nums.sort()

        right = len(nums)-1
        left = 0

        while left < right:
            total = nums[left] + nums[right]

            if total == target: return [left, right]

            elif total > target: right-=1

            else: left+=1

        
        return [0,0]
