class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        def area(i,j):
            w = abs(j-i)
            h = min(heights[j], heights[i])
            return w*h

        l = 0
        r = len(heights)-1
        h = heights
        maxarea = 0
        n = len(h)
        while l < r :
            if l not in range(n) or r not in range(n): return maxarea

            area1 = area(l,r)
            maxarea = max(maxarea, area1)

            if h[l] < h[r]:
                l+=1

            else:
                r-=1

        return maxarea





