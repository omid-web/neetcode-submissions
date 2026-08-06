class Solution:
    def isValid(self, s: str) -> bool:
        pairing = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []

        for c in s:
            if c in pairing:
                if stack and stack[-1] == pairing[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack