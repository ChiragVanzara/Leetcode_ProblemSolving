class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums1 = []
        for i in range(len(nums)):
            if nums[i] == target:
                nums1.append(i)
                break
            
        for j in range(len(nums)-1,-1,-1):
            if nums[j] == target:
                nums1.append(j)
                break
        if len(nums1) == 2:
            return nums1
        else:
            return [-1,-1]
        
