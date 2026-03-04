class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 0
        while(x>=0):
            if 2**x < n:
                x += 1
            elif 2**x == n:
                return True
            else:
                return False