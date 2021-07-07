"""
150. Evaluate Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
"""

#stack

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if (len(tokens) == 1): return int(tokens[0])        
        stack = []   
        for i in range(len(tokens)):
            if tokens[i] not in '+-*/': stack.append(int(tokens[i]))       
            else:
                num1 = stack.pop(0); num2 = stack.pop(0)                
                if (tokens[i] == "+"): stack.append(num2+num1)
                if (tokens[i] == "-"): stack.append(num2-num1)
                if (tokens[i] == "*"): stack.append(num2*num1)
                if (tokens[i] == "/"): stack.append(num2/num1)
        return stack[0]        
