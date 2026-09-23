class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        prev = None

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue

            prev = nums[i]
            slow = i+1
            fast = len(nums)-1
            while slow < fast:
                current = nums[i] + nums[slow] + nums[fast]
                if current == 0:
                    ans.append([nums[i], nums[slow], nums[fast]])
                    slow += 1
                    fast -= 1

                    while slow < len(nums) and nums[slow] == nums[slow-1]:
                        slow += 1
                    
                    while fast > 0 and nums[fast] == nums[fast+1]:
                        fast -= 1


                elif current < 0:
                    slow += 1
                else:
                    fast -= 1
        
        return ans

        