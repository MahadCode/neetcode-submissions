class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_map = {}
        for index, word in enumerate(strs):
            lst = [0] * 26
            for alphabet in word:
                value = ord(alphabet) - ord('a')
                lst[value] += 1
            key = tuple(lst)
            string_map.setdefault(key, []).append(index) 

        ans = []
        for value in string_map.values():
            curr = []
            for v in value:
                curr.append(strs[v])
            
            ans.append(curr)
        
        return ans
                



            