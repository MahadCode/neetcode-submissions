class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = {}
        s = 0
        ans = 0
        for i in range(len(fruits)):
            fruit = fruits[i]
            fruit_count[fruit] = fruit_count.get(fruit,0) + 1

            while len(fruit_count) > 2:
                fruit_count[fruits[s]] -= 1
                if fruit_count[fruits[s]] == 0:
                    fruit_count.pop(fruits[s], None)
                s += 1
            
            ans = max(ans, i-s+1)
        
        return ans



        