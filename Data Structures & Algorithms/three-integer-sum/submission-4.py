class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        print(nums)
        results = []
        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                # print("TOTAL:", total, "NUMBERS", nums[i], nums[l], nums[r])
                
                if total < 0:
                    l +=1
                elif total > 0:
                    r-=1

                else:
                    results.append([nums[i], nums[l], nums[r]])
                    l+=1

                    while l<len(nums)-1 and nums[l] == nums[l-1]:
                        l+=1
                    
                
            
        return results
