class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r = 0
        sm = 0

        while sm < target:
            if r >= len(nums):
                return 0

            sm += nums[r]
            r += 1
        
        ans = r

        l = 0

        while r < len(nums):
        
            while sm >= target:
                ans = min(ans, r-l)   
                sm -= nums[l]
                l += 1
            
            while sm < target:
                if r >= len(nums):
                    return ans

                sm += nums[r]
                r += 1
            ans = min(ans, r-l)
        
        while sm >= target:
            ans = min(ans, r-l)   
            sm -= nums[l]
            l += 1
            
        return ans
            

            
        

        

        