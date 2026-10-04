class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        left = 0

        best = 100001


        total = 0


        for right in range(len(nums)):

            total+=nums[right]

            
            while total >= target:
                best = min(best, right-left+1)
                total-=nums[left]
                left+=1
        

        if best == 100001: return 0

        return best



