class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for i,n in enumerate(nums):
            if nums[i] in duplicates:
                return True
            duplicates[nums[i]] = i
        return False