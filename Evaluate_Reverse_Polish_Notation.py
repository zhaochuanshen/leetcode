'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if len(tokens) == 0:
            return
        stack = []
        operators = ['+','-','*','/']
        for item in tokens:
            try:
                x = int (item)
                stack.append(x)
            except:
                if item not in operators:
                    return
                y = stack.pop()
                z = stack.pop()
                if item == '+':
                    x = z + y
                if item == '-':
                    x = z - y
                if item == '*':
                    x = z * y
                if item == '/':
                    if y == 0:
                        return
                    if y*z < 0:
                        t = z / y
                        if z != t*y:
                            x = t+1
                        else:
                            x = t
                    else:
                        x = z / y
                stack.append(x)
        if len (stack) != 1:
            return
        return stack[0]
