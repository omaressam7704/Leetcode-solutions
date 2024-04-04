class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        sum1 = 0
        product = 1
        for i in s:
            sum1 = sum1 + int(i)
            product = product * int(i)
        return product - sum1