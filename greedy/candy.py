__author__ = 'daming'

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if len(ratings) <= 0:
            return 0

        candies = [0] * len(ratings)
        candies[0] = 1

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
            else:
                candies[i] = 1

        sum = candies[len(ratings)-1]
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] +1

            sum += candies[i]
        # print candies
        return sum

obj = Solution()

print obj.candy([4,5,4,3,2,3])