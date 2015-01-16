__author__ = 'daming'

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q


class Edge:
    def __init__(self, from_point, to_point, weight=1):
        self.from_point = from_point
        self.to_point = to_point
        self.weight = weight
        self.is_visited = False
    def __cmp__(self, other):
        return cmp(self.weight, other.weight)

class Vertex:
    def __init__(self, point):
        self.point = point
        self.is_visited = False
        self.to_here = -1

class TheGridDivTwo:
    def __init__(self):
        self.block_points = set([])
        self.q = Q.PriorityQueue()
        self.points_to_visit = []

    def get_neighbors(self, vertex):
        v_x = vertex.point[0]
        v_y = vertex.point[1]

        neighbors = []
        north = (v_x, v_y+1)
        east = (v_x+1, v_y)
        south = (v_x, v_y-1)
        west = (v_x-1, v_y)

        if north not in self.block_points:
            neighbors.append(north)
        if east not in self.block_points:
            neighbors.append(east)
        if south not in self.block_points:
            neighbors.append(south)
        if west not in self.block_points:
            neighbors.append(west)

        return neighbors


    def find(self, x, y, k):
        for i in range(0, len(x)):
            cur_x = x[i]
            cur_y = y[i]
            self.block_points.add((cur_x, cur_y))

        cur_point = Vertex((0, 0))
        cur_point.to_here = 0
        dest_point = Vertex((k, 0))

        self.points_to_visit.append(cur_point)

        while len(self.points_to_visit) > 0:
            cur_point = self.points_to_visit.pop(0)
            cur_dist = cur_point.to_here
            cur_point.is_visited = True
            cur_point_neighbors = self.get_neighbors(cur_point)

            for i in range(0, len(cur_point_neighbors)):
                if cur_point_neighbors[i].to_here == -1:
                    cur_point_neighbors[i].to_here = cur_dist + 1
                if cur_point_neighbors[i].to_here > cur_dist + 1:
                    cur_point_neighbors[i].to_here = cur_dist + 1

            self.points_to_visit.extend(cur_point_neighbors)



        print self.block_points
        if (1,12) in self.block_points:
            print 'haha'


obj = TheGridDivTwo()
obj.find((1,2,2), (1,2,2),3)

