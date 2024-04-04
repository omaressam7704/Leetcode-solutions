class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ls = []
        for i in range(1, n+1):  # Start from 1 instead of 0
            if i % 3 == 0 and i % 5 == 0:
                ls.append("FizzBuzz")
            elif i % 3 == 0:
                ls.append("Fizz")
            elif i % 5 == 0:
                ls.append("Buzz")
            else:
                ls.append(str(i))
        return ls
