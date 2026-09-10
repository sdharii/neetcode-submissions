class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # can always assume the stack has a 2 numbers in it before an operator
        for char in tokens:
            # addition
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            # subtraction : remember to subtract the bigger number first!
            elif char == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            # multiplication
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            # division : make sure it truncates toward zero, order matters
            elif char == "/":
               a, b = stack.pop(), stack.pop()
               stack.append(int(float(b)/a))
            else:
                stack.append(int(char)) 
        return stack[0]

