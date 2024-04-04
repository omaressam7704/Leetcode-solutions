class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(nums)):
            j = i - 1
            nums[i] = nums[i] + nums[j]
        return nums  