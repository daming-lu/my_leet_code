__author__ = 'daming'

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        start_point = 0
        if len(gas) <= 0:
            return -1

        cur_sum = 0
        i = 0
        justDepart = True
        while justDepart or (i)%len(gas) != start_point:
            cur_sum += gas[i]-cost[i]
            # print 'i : ', i, "cur_sum", cur_sum, ", start_point : ", start_point

            if cur_sum < 0:
                i += 1
                i %= len(gas)
                if i<=start_point:
                    return -1
                start_point = i
                justDepart = True
                cur_sum = 0
            else:
                justDepart = False
                i += 1
                i %= len(gas)
        return start_point

obj = Solution()

g1 = [1,2,333]
c1 = [11,22,33]

print obj.canCompleteCircuit(g1,c1)


g2 = [2,4]
c2 = [3,4]

print obj.canCompleteCircuit(g2,c2)


