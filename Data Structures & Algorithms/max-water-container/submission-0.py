class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        def area(i, j):

            height = min(heights[i], heights[j])

            return height * abs(j-i)

        l = 0
        r = len(heights)-1

        amax = area(r,l)

        while l < r:

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

            amax = max(amax, area(r,l))

        

        return amax
            

