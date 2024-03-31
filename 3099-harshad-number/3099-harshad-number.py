class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 100:
            return 1
        num1 = x % 10
        num2 = x//10
        num3 = num1+num2
        if x % num3 == 0:
            return num3
        else:
            return -1