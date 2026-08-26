class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temp = temperatures

        output = [0]*len(temp)

        stack = []

        for i in range(len(temp)):
            while len(stack) > 0 and temp[stack[-1]] < temp[i]:
                j = stack.pop()

                output[j] = i-j

            stack.append(i)
            
        # print(stack)
        
        return output
