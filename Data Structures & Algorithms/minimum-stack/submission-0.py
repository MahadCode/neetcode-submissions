class MinStack:

    def __init__(self):
        self.l = []
        

    def push(self, val: int) -> None:
        if not self.l:
            self.l.append((val,val))
        else:
            m = self.l[len(self.l)-1][1]
            self.l.append((val,min(val,m)))
        

    def pop(self) -> None:
        self.l.pop()
        

    def top(self) -> int:
        return self.l[-1][0]
        

    def getMin(self) -> int:
        return self.l[-1][1]
        

