class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        result = [-1] * len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            curr = temperatures[i]
            while stk and curr >= temperatures[stk[-1]]:
                stk.pop()
            
            if stk:
                result[i] = stk[-1]

            stk.append(i)
        
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if result[i] >= 0:
                ans[i] = result[i] - i

        return ans





        