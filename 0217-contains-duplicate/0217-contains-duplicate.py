class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        countMap = {}
        for name in nums:
            if name not in countMap:
                countMap[name] = 1
            else:
                countMap[name] += 1
        for key,val in countMap.items():
            if val > 1:
                return True  
        return False