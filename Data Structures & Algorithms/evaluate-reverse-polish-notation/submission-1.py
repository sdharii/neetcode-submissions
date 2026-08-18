class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opStack = []
        operators = ["+", "-", "*", "/"]

        for char in tokens:
            if char not in operators:
                opStack.append(int(char))
            if char == "+":
                opStack.append(opStack.pop() + opStack.pop())
            elif char == "-":
                a, b = opStack.pop(), opStack.pop()
                opStack.append(b - a)
            elif char == "*":
                opStack.append(opStack.pop() * opStack.pop())
            elif char == "/":
                a, b = opStack.pop(), opStack.pop()
                opStack.append(int(float(b)/a))
        return opStack[0]



