class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num = len(nums)
        i = 0
        while i < num:
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
            i+=1