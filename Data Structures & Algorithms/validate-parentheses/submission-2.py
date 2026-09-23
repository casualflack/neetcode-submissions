class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = {'(', '[', '{'}
        right = {')' : '(', ']' : '[', '}' : '{'}
        
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if len(stack) == 0 or stack.pop() != right[c]:
                    return False
        
        return True if len(stack) == 0 else False


        