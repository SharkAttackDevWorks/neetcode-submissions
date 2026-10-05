class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)

        intervals.sort()

        output = []


        for x in intervals:
            if len(output)<1: output.append(x); continue

            startX, endX = x

            startP, endP = output[-1]

            if startX < endP:
                output[-1] = startP, max(endP, endX)

            else:
                output.append(x)




        return output