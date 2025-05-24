class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)

        for i in range(m):
            if haystack[i] == needle[0]:
                s = haystack[i:i+n]
                if s == needle:
                    return i
        return -1
        
        