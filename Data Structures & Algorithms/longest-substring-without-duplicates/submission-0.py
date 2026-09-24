class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1
        
        l = 0
        r = 0
        existence_dict = {}

        while r < len(s):
            curr = s[r]
            if existence_dict.get(curr, False):
                break
            
            existence_dict[curr] = True
            r += 1
        
        ans = r

        while r < len(s):
            curr = s[r]
            while l <= r and existence_dict.get(curr, False):
                existence_dict[s[l]] = False
                l += 1

            ans = max(ans, r-l+1)
            existence_dict[curr] = True
            r += 1
        
        return ans

        
            

            
                
            
        