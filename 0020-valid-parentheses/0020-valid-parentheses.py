class Solution(object):
    def isValid(self,s):
        if len(s) % 2 != 0: 
            return False
        stack = []
        mapping = {"(": ")", "{": "}", "[": "]"}
    
        for char in s:
            if char in mapping:  
                stack.append(char)
            else:  
                if not stack:  
                    return False
                if mapping[stack.pop()] != char:  
                    return False
    

        return not stack


