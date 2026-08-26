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
            c = (l+r)//2

            if c > 0 and nums[c-1] > nums[c]:
                pivot = c
                break
            elif c < n-1 and nums[c] > nums[c+1]:
                pivot = c+1
                break

            if nums[0] < nums[c]:
                l = c+1
            else:
                r = c-1

        # print(pivot)
        
        subnums = None

        base = 0

        if pivot is None:
            subnums = nums

        elif target >= nums[0]:
            subnums = nums[0:pivot+1]
        
        else:
            # print("else")
            subnums = nums[pivot:n]
            base = pivot

        # print(subnums)

        n = len(subnums)
        l = 0
        r = n-1

        while l <=r:
            c = (l+r)//2

            if subnums[c]  == target:
                return c+base
            

            if subnums[c] < target:
                l = c+1

            else:
                r = c-1


        return -1


