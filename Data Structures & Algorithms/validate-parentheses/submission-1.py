class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        s = list(s)

        for x in s:
            print(x)
            print(stack)
            if x in "([{":
                stack.append(x)
            
            else:
                if len(stack) > 0:
                    y = stack.pop()
                else:
                    continue
                if y == '[' and x == ']':
                    continue
                elif y == '(' and x == ')':
                    continue
                elif y == '{' and x == '}':
                    continue
                else:
                    return False

        if len(stack) > 0:
            return False
        

        return True
