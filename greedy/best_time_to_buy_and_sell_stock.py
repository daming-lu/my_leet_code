__author__ = 'daming'


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices)<=1:
            return 0
        cur_min = prices[0]
        cur_max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] < cur_min:
                cur_min = prices[i]
            if prices[i] - cur_min > cur_max_profit:
                cur_max_profit = prices[i] - cur_min
        return cur_max_profit
