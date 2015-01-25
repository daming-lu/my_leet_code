__author__ = 'daming'
class PeacefulLine:
    def makeLine(self, x):
        most = 0
        all = 0
        marks = {}
        for e in x:
            if e in marks:
                marks[e] += 1
            else:
                marks[e] = 1
            all += 1
            if marks[e] > most:
                most = marks[e]

        if all-most < most-1:
            return 'impossible'
        return 'possible'

class TravellingSalesmanEasy:
    def getMaxProfit(self, M, profit, city, visit):
        most_valuable_in_city = {}
        for i in range(len(profit)):
            if city[i] in most_valuable_in_city:
                most_valuable_in_city[city[i]].append(profit[i])
            else:
                most_valuable_in_city[city[i]] =[]
                most_valuable_in_city[city[i]].append(profit[i])

        result = 0
        for e in visit:
            if e in most_valuable_in_city:
                most_valuable_in_city[e].sort(reverse=True)
        # print most_valuable_in_city
        for e in visit:
            if e in most_valuable_in_city and len(most_valuable_in_city[e])>0:
                result += most_valuable_in_city[e].pop(0)
        return result

obj =TravellingSalesmanEasy()
print obj.getMaxProfit(1,[3,5,2,6,4],[1,1,1,1,1],[1,1,1])