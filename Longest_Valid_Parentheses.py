'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        maxlength = 0
        right = 0
        current = 0
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if len(stack) != 0 and s[ stack[-1] ] =='(':
                    t = stack.pop()
                    last = -1
                    if len(stack) != 0:
                        last = stack[-1]
                    current = i - last
                    maxlength = max(maxlength, current)
                else:
                    stack.append(i)
        return maxlength
