class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        l=0
        r=n-1

        pivot = None

        if n == 1:
            if nums[0] == target:
                return 0
            return -1

        while l<=r:
            c= (l+r)//2

            if target == nums[c]:
                return c

            if target <= nums[l]:
                l = c+1

            else:
                r = c-1
                

        return -1