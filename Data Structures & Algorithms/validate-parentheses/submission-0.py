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
                y = stack.pop()
                if y == '[' and x == ']':
                    continue
                elif y == '(' and x == ')':
                    continue
                elif y == '{' and x == '}':
                    continue
                else:
                    return False

        

        return True
