__author__ = 'daming'
class Solution_Mine:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        DP = [len(A) for a in A]
        for i in range(len(A)-1, -1, -1):
            if i == len(A)-1:
                DP[i] = 0
                continue
            if A[i] + i>=len(A)-1:
                DP[i] = 1
                continue

            # for j in range(i, i+A[i]+1):
            for j in range(i+A[i], i-1, -1):
                if j>=len(A):
                    break
                if 1+DP[j] < DP[i]:
                    DP[i] = 1+DP[j]
                if DP[i] <= 2:
                    break
        # print DP
        return DP[0]


class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A)<=1:
            return 0
        cur_min_steps = 1
        cur_index = 0
        cur_max_index = A[0]
        next_max_index = cur_max_index
        while cur_index<len(A) and cur_index<=cur_max_index:
            if cur_index == len(A)-1:
                return cur_min_steps
            if A[cur_index]+cur_index > next_max_index:
                next_max_index = A[cur_index]+cur_index

            cur_index += 1
            if cur_index > cur_max_index:
                cur_max_index = next_max_index
                next_max_index = A[cur_index]+cur_index
                cur_min_steps +=1


obj = Solution()

print obj.jump([111])