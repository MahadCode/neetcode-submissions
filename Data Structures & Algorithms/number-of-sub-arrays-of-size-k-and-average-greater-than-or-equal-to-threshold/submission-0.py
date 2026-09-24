class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    
        i = 0
        s = 0
        count = 0
        while i < k:
            s += arr[i]
            i += 1
    
        avg = s // k

        if avg >= threshold:
            count += 1
    
        l = 0
        while i < len(arr):
            s = s - arr[l] + arr[i]
            avg = s // k
            if avg >= threshold:
                count += 1
        
            i += 1
            l += 1
    
        return count


        