class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        found_char = False

        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                count += 1
                found_char = True
            elif found_char:
                # We found space *after* counting some characters, so break
                break

        return count