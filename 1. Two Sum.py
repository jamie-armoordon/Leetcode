#Solution for https://leetcode.com/problems/two-sum/
#By Jamie Armoordon

class Solution(object):
    def twoSum(self, nums, target):
        prev_map =  {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff],i]
            prev_map[n] = i
        return
