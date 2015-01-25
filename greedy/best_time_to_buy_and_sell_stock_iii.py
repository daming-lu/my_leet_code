__author__ = 'daming'

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices)<=1:
            return 0

        # from left
        from_left = []
        cur_min = prices[0]
        cur_max_profit = 0
        for i in range(0,len(prices)):
            if prices[i] < cur_min:
                cur_min = prices[i]
            if prices[i] - cur_min > cur_max_profit:
                cur_max_profit = prices[i] - cur_min
            from_left.append(cur_max_profit)

        # from right
        from_right = []
        cur_max = prices[-1]
        cur_max_profit = 0
        for i in range(len(prices)-1,-1,-1):
            if prices[i] > cur_max:
                cur_max = prices[i]
            if cur_max - prices[i] > cur_max_profit:
                cur_max_profit = cur_max - prices[i]
            from_right.append(cur_max_profit)

        from_right.reverse()
        # print from_left
        # print from_right
        final_max = 0
        for i in range(0,len(prices)):
            if from_left[i]+from_right[i] > final_max:
                final_max = from_left[i]+from_right[i]

        return final_max


obj = Solution()
print obj.maxProfit([0,2,1,2,-3,-1,-2,0,3])