class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dict1 = {}
        for ch in string.punctuation:
            paragraph = paragraph.replace(ch, " ")
        words = paragraph.lower().split()
        
        for word in words:
            if word not in banned:
                if word in dict1:
                    dict1[word] += 1
                else:
                    dict1[word] = 1

        return max(dict1, key=dict1.get)
                