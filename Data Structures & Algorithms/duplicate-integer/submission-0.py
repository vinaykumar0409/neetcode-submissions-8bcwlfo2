class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = len(set(nums))
        return s != len(nums)