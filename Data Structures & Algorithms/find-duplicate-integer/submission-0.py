class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        slow = 0
        fast = nums[slow]

        while nums[slow] != nums[fast] and slow < len(nums)-1:
            
            slow+=1
            fast = nums[slow]

        return nums[slow]