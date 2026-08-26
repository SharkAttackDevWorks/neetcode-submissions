class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #without using division


        forwardmul = []

        for x in nums:
            if len(forwardmul) == 0:
                forwardmul.append(x)
            else:
                forwardmul.append(forwardmul[-1]*x)

        backmul = []

        revnums = nums [::-1]

        for x in revnums:
            if len(backmul) == 0:
                backmul.append(x)
            else:
                backmul.append(backmul[-1]*x)

        backmul = backmul[::-1]

        result = []

        for i in range(len(nums)):
            if i == 0:
                result.append(backmul[1])
            elif i == len(nums)-1:
                result.append(forwardmul[len(nums)-1-1])

            else:

                result.append(forwardmul[i-1]* backmul[i+1])

            
        return result

