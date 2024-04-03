class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for i in nums:
            count[i] += 1
        i = 0
        for n in range(len(count)):
            for j in range(count[n]):
                nums[i] = n
                i+=1
        return nums