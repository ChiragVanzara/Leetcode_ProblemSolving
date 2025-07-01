class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)  # Remove duplicates
        if len(nums) < 3:
            return max(nums)
        nums = list(nums)
        nums.sort(reverse=True)
        return nums[2]  # t