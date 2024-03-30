class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num = 0
        while num < len(nums):
            if nums[num] == 0:
                nums.remove(0)
                nums.append(0)
            num+=1