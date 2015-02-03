__author__ = 'daming'
class Solution_Uber:
    def workhorse(self, n, start_point, edge_length):
        if edge_length<1:
            return

        # top edge
        for i in range(start_point, start_point+edge_length):
            print n[start_point][i]," ",

        # right edge
        for i in range(start_point+1, start_point+1+edge_length-2):
            print n[i][len(n)-1-start_point]," ",

        # bottom edge
        if start_point+edge_length-1 != start_point:
            for i in range(start_point+edge_length-1, start_point-1, -1):
                print n[len(n)-1-start_point][i]," ",

        # left edge
        for i in range(len(n)-1-start_point-1, start_point, -1):
            print n[i][start_point]," ",

        self.workhorse(n, start_point+1, edge_length-2)

    # @return a list of lists of integer
    def generateMatrix(self, n):
        edge_length = len(n)
        start_point = 0
        self.workhorse(n, start_point, edge_length)


class Solution:
    def workhorse(self, n, start_point, edge_length, counter):
        if edge_length<1:
            return

        # top edge
        for i in range(start_point, start_point+edge_length):
            n[start_point][i] = counter
            counter += 1

        # right edge
        for i in range(start_point+1, start_point+1+edge_length-2):
            n[i][len(n)-1-start_point] = counter
            counter += 1

        # bottom edge
        if start_point+edge_length-1 != start_point:
            for i in range(start_point+edge_length-1, start_point-1, -1):
                n[len(n)-1-start_point][i] = counter
                counter += 1

        # left edge
        for i in range(len(n)-1-start_point-1, start_point, -1):
            n[i][start_point] = counter
            counter += 1

        self.workhorse(n, start_point+1, edge_length-2, counter)
    # @return a list of lists of integer
    def generateMatrix(self, n):
        ans = [[-1 for i in range(n)] for i in range(n)]
        counter = 1
        self.workhorse(ans, 0, n, counter)
        return ans

test1 = [[1,2,3],[4,5,6],[7,8,9]]
test2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

obj = Solution_Uber()

# obj.generateMatrix(test2)

obj2 = Solution()
obj2.generateMatrix(4)