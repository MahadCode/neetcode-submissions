class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        s = 0
        product = 1
        prefix_count = 0
        for i in range(len(nums)):
            product = product * nums[i]
            prefix_count += 1

            while s <= i and product >= k:
                product = product // nums[s]
                s += 1
                prefix_count -= 1
            
            if prefix_count > 0:
                ans += prefix_count
        
        return ans

