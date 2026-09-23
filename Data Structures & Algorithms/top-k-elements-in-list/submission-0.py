class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        

        lst = sorted((count.items()), key=lambda x:x[1], reverse=True)

        lst = lst[:k]

        return [x[0] for x in lst]


        