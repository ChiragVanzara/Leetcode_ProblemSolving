class Solution:
    def convertToBase7(self, num: int) -> str:
        negative = num < 0
        if num == 0:
            return '0'
        num = abs(num)
        s = ""
        while num > 0:
            remainder = num % 7
            s = str(remainder) + s
            num //= 7

        if negative:
            s = "-" + s
        return s
