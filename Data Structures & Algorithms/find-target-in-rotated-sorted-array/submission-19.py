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

            #nums[c] = 5 
            #nums[l] = 3
            #nums[r] = 2

            if  nums[l] <= nums[c]:
                if nums[l] <= target < nums[c]:
                    r = c-1
                else:
                    l = c+1

            else:
                if nums[c] < target <= nums[r]:
                    l = c+1

                else:
                    r=c-1


        return -1
