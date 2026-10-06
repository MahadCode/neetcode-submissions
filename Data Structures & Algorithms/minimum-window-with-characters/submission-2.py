class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic_t = {}

        required = 0
        for n in t:
            if dic_t.get(n, 0) == 0:
                dic_t[n] = 1
                required += 1
            else:
                dic_t[n] += 1
        
        dic_s = {}
        l = 0
        ans = 100000
        ans_str = ""
        formed = 0

        for i , curr in enumerate(s):

            dic_s[curr] = dic_s.get(curr,0) + 1
            if dic_t.get(curr,0) and dic_s[curr] == dic_t[curr]:
                formed += 1

            while formed == required:
                if ans > i-l+1:
                    ans = i-l+1
                    ans_str = s[l:i+1]
                

                dic_s[s[l]] -= 1
                if dic_t.get(s[l],0) and dic_s[s[l]] < dic_t[s[l]]:
                    formed -= 1

                l += 1
            
        return ans_str


        

        