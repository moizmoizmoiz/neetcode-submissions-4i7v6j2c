class Solution:
    def scoreOfString(self, s: str) -> int:
        n = 0
        size = len(s)
        arr = list(s)
        ans = 0
        
        for x in range(0, size-1):
                value = abs(ord(arr[x+1]) - ord(arr[x]))
                ans = ans + value
        return ans