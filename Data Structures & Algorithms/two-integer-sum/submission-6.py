class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsactual = nums[:]
        nums.sort()

        right = len(nums)-1
        left = 0

        def returnfunction(l, r, n):

            i = n.index(l)
            j = n.index(r)

            if i == j:
                j = n[i:].index(r)
                j = i+j
            
            return i, j

        while left < right:
            total = nums[left] + nums[right]

            if total == target: 
                i, j = returnfunction(nums[left], nums[right], numsactual)
                return [i, j]

            elif total > target: right-=1

            else: left+=1


        return [0,0]
