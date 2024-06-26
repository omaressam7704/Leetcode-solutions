class Solution(object):
    def __init__(self):
        self.memo = {}

    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.memo:
            return self.memo[n]
        
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            result = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            self.memo[n] = result
            return result