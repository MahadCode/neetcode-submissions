class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow =  1
        flg = True
        for fast in range(1, len(nums)):
            if nums[fast] == nums[slow-1] and flg:
                nums[slow] = nums[fast]
                slow += 1
                flg = False
            
            if nums[fast] != nums[slow-1]:
                nums[slow] = nums[fast]
                slow += 1
                flg = True
            
        return slow



        