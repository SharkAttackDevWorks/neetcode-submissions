class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        


        profit = 0
        print(profit)

        amin = prices[0]

        for aprice in prices:

            profit = max(aprice-amin , profit)

            amin = min(amin, aprice)

        return int(profit)


