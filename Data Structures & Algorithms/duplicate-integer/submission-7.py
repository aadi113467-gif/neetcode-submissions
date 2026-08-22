class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for i,n in enumerate(nums):
            if n in duplicates:
                return True
            duplicates[n] = i
        return False