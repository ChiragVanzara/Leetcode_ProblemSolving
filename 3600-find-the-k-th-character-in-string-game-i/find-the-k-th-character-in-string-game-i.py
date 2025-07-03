class Solution:
    def kthCharacter(self, k: int) -> str:
        s = 'ab'
        n = k
        for _ in range(k):
            new_s = ""
            for char in s:
                next_c = chr(ord(char) + 1)
                new_s += char + next_c
            s = new_s
            if len(s)<=k:
                continue
            else:
                return s[k-1]
    