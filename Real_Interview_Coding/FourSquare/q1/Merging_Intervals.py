__author__ = 'daming'
import fileinput
import sys

class Solution:
    def findNonCoverIntervals(self):
        input_intervals = []
        for line in fileinput.input():
            pieces = line.split()
            if len(pieces) != 2:
                print >> sys.stderr, "Interval ", pieces, ' does not contain 2 numbers (start,end)'
                sys.exit(1)
            input_intervals.append((int(pieces[0]), int(pieces[1])))

        if len(input_intervals) <= 1:
            return []

        input_intervals = sorted(input_intervals, key=lambda x:x[0])

        merged_intervals = [input_intervals[0]]
        holes = []
        for i in range(1, len(input_intervals)):
            cur_interval = input_intervals[i]
            if cur_interval[0] > merged_intervals[-1][1]:
                # no overlapping
                holes.append((merged_intervals[-1][1], cur_interval[0]))
                merged_intervals.append(cur_interval)
            else:
                # has overlapping with prev interval
                if cur_interval[1] > merged_intervals[-1][1]:
                    last_interval = merged_intervals.pop()
                    new_last_interval = (last_interval[0], cur_interval[1])
                    merged_intervals.append(new_last_interval)
        return holes

obj = Solution()
print obj.findNonCoverIntervals()