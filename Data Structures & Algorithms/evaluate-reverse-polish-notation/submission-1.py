class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['-', '+', '/', '*']
        stack = []


        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                print(a,b)
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(b - a)
                elif t == '*':
                    stack.append(a * b)
                elif t == '/':
                    stack.append(int(b / a))


        print(stack)
        return int(stack.pop())



