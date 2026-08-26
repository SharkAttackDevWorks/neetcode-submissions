class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        aset = set(nums)

        left = 0
        right = len(nums)-1

        results = []

        while left < right:
            
            middle = (left+right) // 2

            target = nums[left] + nums[right]

            while middle > left and middle < right:
                if target == nums[middle]:
                    results.append(nums[left], nums[middle], nums[right])
                    left +=1

                elif target > nums[middle]:
                    right-=1

                else:
                    left +=1

        
        return results
                
            
