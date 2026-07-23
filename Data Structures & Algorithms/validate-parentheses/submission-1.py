class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closer = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        if len(s) % 2 > 0: return False

        for _ in s:
            if _ in closer:
                if stack and stack[-1] == closer[_]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(_)

        return True if not stack else False
                