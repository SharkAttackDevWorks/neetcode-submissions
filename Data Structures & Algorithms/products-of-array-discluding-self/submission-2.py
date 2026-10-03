class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lr = []
        rl = []

        rever = nums[::-1]

        for x in nums:
            if len(lr)<1:
                lr.append(x)
            else:
                lr.append(x*lr[-1])
        
        for x in rever:
            if len(rl) < 1:
                rl.append(x)
            else:
                rl.append(x*rl[-1])

        
        output = []

        rl = rl[::-1]
        # print(lr)
        # print(rl)

        for i in range(len(nums)):
            

            if i-1 >= 0: num1 = lr[i-1]
            else: num1 = 1

            if i+1 <= len(nums)-1 : num2 = rl[i+1]
            else: num2 =1

            output.append(num1*num2)

        return output
                