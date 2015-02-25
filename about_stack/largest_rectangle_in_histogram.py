__author__ = 'daming'
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        my_stack = [(0,-1)] # height, index
        height.append(0)
        cur_max = 0
        for i in range(0, len(height)):
            if height[i] >= my_stack[-1][0]:
                my_stack.append((height[i],i))
            elif height[i] < my_stack[-1][0]:
                while my_stack[-1][0] > height[i]:
                    cur_height = my_stack.pop()
                    cur_area = cur_height[0] * (i - my_stack[-1][1] - 1)
                    if cur_area > cur_max:
                        cur_max = cur_area
                my_stack.append((height[i],i))
        return cur_max

obj = Solution()

print obj.largestRectangleArea([4,4,4,6])



