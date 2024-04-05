class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num1 = int(''.join(map(str, digits)))
        num1 = num1 + 1
        if num1 == 0:
            return [0]
        digits = []
        while num1 > 0:
            digit = num1 % 10
            digits.append(digit)
            num1 //= 10
        digits.reverse()
        return digits