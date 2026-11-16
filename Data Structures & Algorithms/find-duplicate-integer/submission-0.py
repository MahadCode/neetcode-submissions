class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = 0
        f = 0
        flg = True
        while flg or nums[s] != nums[f]:
            s = nums[s]
            f = nums[nums[f]]
            flg = False
        
        s = 0
        while nums[s] != nums[f]:
            s = nums[s]
            f = nums[f]
        
        return nums[s]

        