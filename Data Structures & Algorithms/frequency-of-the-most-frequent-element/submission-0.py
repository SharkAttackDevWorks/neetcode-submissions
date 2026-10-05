class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        left = 0

        best = 0

        asum = 0

        nums.sort()


        for right in range(0, len(nums)):

            asum+=nums[right]

            while  (right-left+1)*nums[right] -asum > k:
                asum-=nums[left]
                left+=1

            best = max(best, right-left+1)



        return best