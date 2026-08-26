class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxa = 0
        mina = float('inf')
        amax = 0
        p = prices


        for i in range(len(p)):
            

            mina = min(p[i], mina)


            amax = max(amax, p[i] - mina)





        return amax

