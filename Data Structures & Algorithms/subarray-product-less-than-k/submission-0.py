class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        output = 0

        left = 0

        product = 1.0


        for right in range(len(nums)):
            product*= nums[right]

            while product >= k and right>left:
                product/=nums[left]
                left+=1


            if product < k:
                n = right-left+1
                output+=n


        
        return int(output)

        





