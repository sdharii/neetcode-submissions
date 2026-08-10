class Solution:
    def isValid(self, s: str) -> bool:
        """
        input: string (s) containing different brackets
        output: bool -> true is s is a valid str, otherwise false
        constraints:
            - every open bracket has a corresponding close bracket
            - open brackets should be closed in the correct order
            - every close brack has a corresponding open bracket
        edge cases:
            - 
        implementation:
            create a stack using an array
            create a dictionary w/ closing brackets as the key & open brackets as the value

            loop through string
                if char in dictionary
                    1. if its a closed bracket, pop top item from stack
                        - top item in stack MUST correspond to the closed bracket type
                        - check if stack is empty
                        - if it doesnt meet the prior requirements, return false
                    2. if its an open bracket, append to stack
            return true if stack is empty, otherwise false  
        """

        myStack = []
        myDict = {")" : "(", "}" : "{", "]" :"["}

        for char in s:
            if char in myDict:
                # if its a closed bracket
                if myStack and myStack[-1] == myDict[char]:
                    myStack.pop()
                else:
                    return False 
            else:
                myStack.append(char)
        if not myStack:
            return True
        return False
