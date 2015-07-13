__author__ = 'daming'

class Solution:
    def notIntersect(self, A, B, C, D, E, F, G, H):
        if C <= E or A >= G or F >= D or H <= B:
            return True
        return False

    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        twoSum = self.calcArea((A,B), (C,D)) + self.calcArea((E,F), (G,H))
        if self.notIntersect(A, B, C, D, E, F, G, H):
            return twoSum
        bottom_left = (max(A,E), max(B,F))
        top_right = (min(C,G), min(D,H))
        return twoSum - self.calcArea(bottom_left, top_right)

    def calcArea(self, bottom_left, top_right):
        return (top_right[0] - bottom_left[0]) * (top_right[1] - bottom_left[1])

obj = Solution()

print obj.computeArea(-2, -2, 2, 2, 1, -3, 3, -1)