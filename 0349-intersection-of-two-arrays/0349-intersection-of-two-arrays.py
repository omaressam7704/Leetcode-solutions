class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ls = []
        for i in nums1:
            if i in nums2:
                if i not in ls:
                    ls.append(i)
        return ls