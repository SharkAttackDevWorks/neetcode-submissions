class Solution:
    def trap(self, height: List[int]) -> int:
        

        def vol (i, height):

            if i == 0:
                return 0, None, None
            if i == len(height)-1:
                return 0, 0, 0
            
            l = i-1
            r = i+1
            
            lmax = 0
            lidx = None
            rmax = 0
            ridx = None

            while l >= 0 and height[l] > lmax:
                lmax = height[l]
                lidx = l
                l-=1
                        
            while r <= len(height)-2 and height[r+1] >= lmax:
                rmax = height[r]
                ridx = r
                r+=1
            
            hmin = min(lmax, rmax)

            result = 0

            if hmin <= 0:
                return 0, None, None

            for h in range(lidx, r-1):

                result += hmin-height[h]
            
            # print("i =", i)
            # print("area =", result, lidx, ridx)
            return result, lidx, ridx


        result = 0

        i = 0
        
        while i < len(height):

            volume = vol(i, height)
            result, lidx, ridx = volume
            print("i =", i)
            print("area =", result, lidx, ridx)


            if volume[0] > 0 :
                result+=volume[0]
                i = volume[2]+1
            
            else:
                i+=1
        
        return result