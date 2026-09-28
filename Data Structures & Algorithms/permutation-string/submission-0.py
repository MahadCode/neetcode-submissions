class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = [0] * 26
        for i in range(len(s1)):
            mp[ord(s1[i])-ord('a')] = mp[ord(s1[i])-ord('a')]+1
        
        l = 0
        p = 0
        mp1 = [0] * 26
        for i in range(len(s2)):
            mp1[ord(s2[i])-ord('a')] = mp1[ord(s2[i])-ord('a')]+1
            l += 1

            if l > len(s1):
                l -= 1
                ch = s2[p]
                mp1[ord(ch)-ord('a')] = mp1[ord(ch)-ord('a')] - 1
                p += 1

            if mp == mp1:
                return True
            
        
        return False

            







        