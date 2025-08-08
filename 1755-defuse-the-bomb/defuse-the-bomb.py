class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        code1 = [0] * (n)
        if k == 0:
            return code1
        else:
            for i in range(n):
                temp = 0
                if k > 0:
                    for j in range(1, k + 1):
                        temp += code[(i + j) % n]
                else:
                    for j in range(1, -k + 1):
                        temp += code[(i - j + n) % n]
                code1[i] = temp
            return code1
