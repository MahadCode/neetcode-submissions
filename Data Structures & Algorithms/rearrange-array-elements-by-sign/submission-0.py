class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 0
        flag = True
        ans = []
        while (pos < len(nums) or neg < len(nums)):
            if flag:
                while pos < len(nums) - 1 and nums[pos] < 0:
                    pos += 1
                
                if pos < len(nums) and nums[pos] > 0:
                    ans.append(nums[pos])

                pos += 1
                flag = False

            else:
                while neg < len(nums) - 1 and nums[neg] > 0:
                    neg += 1
                
                if neg < len(nums) and nums[neg] < 0:
                    ans.append(nums[neg])

                neg += 1
                flag = True
        
        return ans


        