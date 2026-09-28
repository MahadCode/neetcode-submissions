class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = k

        count = 0
        zeros = 0
        l = 0

        for i in range(len(nums)):
            curr = nums[i]
            if curr == 0:
                zeros += 1
            
            while zeros > k:
                    if nums[l] == 0:
                        zeros -= 1
                    l += 1

            ans = max(ans, i-l+1)
                
        
        return ans
                
            
            
            


            






            

        