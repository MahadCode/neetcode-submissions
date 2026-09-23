class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(nums):
            required = target - num
            required_index = mp.get(required, -1)
            if required_index != -1:
                return [required_index, i]

            mp[num] = i
            


        