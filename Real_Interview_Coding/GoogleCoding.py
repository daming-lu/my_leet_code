__author__ = 'daming'


class Library:
    def __init__(self, N):
        self.matrix = [[None for i in range(N)] for j in range(N)]
        self.N = N
    def update(self, r, c, v):
        if r<0 or r>=self.N or c<0 or c>=self.N:
            return None

        self.matrix[r][c] = v

    def query(self, x1,y1, x2,y2):
        # check all are in bound
        start_row = min(x1,x2)
        end_row = max(x1,x2)

        start_col = min(y1,y2)
        end_col = max(y1,y2)

        result = 0
        for i in range(start_row, end_row+1):
            for j in range(start_col, end_col+1):
                result += self.matrix[i][j]

        return result

    def disp(self):

        for i in range(self.N):
            for j in range(self.N):
                print self.matrix[i][j]," ",
            print "\n"


#

class Library2:
    def __init__(self, N):
        self.matrix = [[0 for i in range(N)] for j in range(N)]
        self.sums = [[0 for i in range(N)] for j in range(N)]
        self.N = N
    def update(self, r, c, v):
        if r<0 or r>=self.N or c<0 or c>=self.N:
            return None
        origin_v = self.matrix[r][c]

        diff = v - origin_v
        self.matrix[r][c] = v
        for i in range(r, self.N):
            for j in range(c, self.N):
                self.sums[i][j] += diff

    def query(self, x1,y1, x2,y2):
        # check all are in bound
        start_row = min(x1,x2)
        end_row = max(x1,x2)

        start_col = min(y1,y2)
        end_col = max(y1,y2)

        result = 0
        for i in range(start_row, end_row+1):
            for j in range(start_col, end_col+1):
                result += self.matrix[i][j]

        return result

    def disp(self):

        for i in range(self.N):
            for j in range(self.N):
                print self.matrix[i][j]," ",
            print "\n"

#
N = 4

obj = Library(N)

for i in range(N):
    for j in range(N):
        obj.update(i,j,i+j)

obj.disp()

print obj.query(3,2,1,1)

