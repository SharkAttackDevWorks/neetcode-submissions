class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        speed = 1

        time = float("inf")


        while time > h:
            time = 0

            for pile in piles:

                time+= math.ceil(pile/speed)

            speed+=1
            
        
        return speed-1



