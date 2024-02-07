class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        l = 0
        window = []
        currSum = 0
        res = 0
        
        for r in range(len(arr)):
            window.append(arr[r])
            currSum += arr[r]
            
            if len(window) == k:
                avg = currSum/k
                if avg >= threshold:
                    res += 1
                window.remove(arr[l])
                currSum -= arr[l]
                l += 1
        return res
            
        