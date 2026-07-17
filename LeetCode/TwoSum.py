class Solution:
    def twoSum(self, nums, target):
        mp = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mp:
                return [mp[diff], i]
            mp[nums[i]] = i
