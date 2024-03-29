class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for op in operations:
            if op.isdigit() or (op[0] == '-' and op[1:].isdigit()): 
                stack.append(int(op))
            elif op == 'C' and stack:
                stack.pop()
            elif op == 'D' and len(stack) > 0:
                stack.append(stack[-1] * 2)
            elif op == '+' and len(stack) > 1:
                stack.append(stack[-1] + stack[-2])
        return sum(stack)
