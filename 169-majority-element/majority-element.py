class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        count = 0
        major = 0

        for i in nums:
            dic[i] = dic.get(i,0) + 1
            if dic[i] > count:
                count = dic[i]
                major = i
        
        return major
        