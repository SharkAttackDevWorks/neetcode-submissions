class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)

        l = 0
        r = n-1

        start = nums[0]
        end = nums[n-1]

        if start <= end:
            return start

        

        while l <= r:

            c = (l+r)//2

            if c < n-1 and nums[c] < nums[c-1]:
                return nums[c]
            elif nums[c] > nums[c+1]:
                return nums[c+1]


            if nums[c] > end:
                l = c+1
            else:
                r = c-1

