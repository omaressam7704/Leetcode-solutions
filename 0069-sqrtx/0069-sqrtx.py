class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x == 0 or x == 1):
            return x
        return int(floor(math.sqrt(x)))