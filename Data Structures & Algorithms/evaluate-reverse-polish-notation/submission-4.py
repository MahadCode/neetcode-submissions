class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token in ['+','-','*','/']:
                s = stk.pop()
                f = stk.pop()
                if token == '+':
                    stk.append(f+s)
                elif token == '-':
                    stk.append(f-s)
                elif token == '*':
                    stk.append(f*s)
                elif token == '/':
                    stk.append(int(f/s))
            else:
                stk.append(int(token))
        
        return stk[0]
                
        