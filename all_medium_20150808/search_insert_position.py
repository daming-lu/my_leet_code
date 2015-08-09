
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0

        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        if len(nums) == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1

        left = 0
        right = len(nums)-1

        while left < right:
            if left + 1 == right:
                if nums[left] == target:
                    return left
                elif target <= nums[right]:
                    return left+1
                return right+1

            mid = (left + right)/2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid