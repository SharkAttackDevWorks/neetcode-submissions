class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def time(speed, piles):
            
            result = 0

            for pile in piles:

                result+= math.ceil(pile/speed)


            return result
            
        
        l = 1
        r = max(piles)
        c = (l+r)//2

        while l <= r:



            if time(c, piles) > h:
                l = c+1
                c = (l+r)//2

            else:
                r = c-1
                c = (l+r)//2


        print(l, r)
        
        return c+1



