__author__ = 'daming'

class TheConsecutiveIntegersDivTwo:
    def find(self, numbers, k):
        if k == 1:
            return 0
        numbers = list(numbers)
        numbers.sort()
        num_ops = -1
        for i in range(0, len(numbers)-1):
            cur_num_ops = self.calc_ops(numbers[i], numbers[i+1])
            if num_ops == -1:
                num_ops = cur_num_ops
            elif cur_num_ops < num_ops:
                num_ops = cur_num_ops

        return num_ops

    def calc_ops(self, a, b):
        dist = a-b
        if dist<0:
            dist = -dist
        if dist == 0:
            return 0
        else:
            return dist-1

obj = TheConsecutiveIntegersDivTwo()
print obj.find((-96, -53, -511, -24, 6, 5),2)