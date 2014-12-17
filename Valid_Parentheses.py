'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution:
    # @return a boolean
    def isValid(self, s):
        l = list(s)
        stack = []
        for c in l:
            if c =='(' or c == '{' or c == '[':
                stack.append(c)
            if c ==')':
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if x != '(':
                    return False
            if c =='}':
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if x != '{':
                    return False
            if c ==']':
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if x != '[':
                    return False   
        if len(stack) > 0:
            return False
        return True
