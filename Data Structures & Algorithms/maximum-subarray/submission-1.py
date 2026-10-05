class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        trailmax = []

        for i in range(len(nums)):
            if len(trailmax) < 1: trailmax.append(nums[i]); continue


            trailmax.append(max(nums[i], trailmax[-1]+nums[i]))


        
        return max(trailmax)



