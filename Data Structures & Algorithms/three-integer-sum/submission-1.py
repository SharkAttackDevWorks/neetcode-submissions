class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()



        results = []


        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
 
            l = i+1
            r = len(nums)-1

            while l < r:
                total = nums[l] + nums[r] + nums[i]            


                if total < 0:
                    l+=1
                elif total > 0:
                    r-=1
                else:
                    results.append([nums[l], nums[i], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1]:
                        l+=1

            
        return results

            
