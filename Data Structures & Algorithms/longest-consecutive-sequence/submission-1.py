class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return 1
        if len(nums) == 0 :
            return 0
        a = sorted(set(nums))
        print(a)
        streak = 1
        ans = 1
        for i in range(1, len(a)):
            prev = a[i-1]
            cur = a[i]
            if prev + 1 == cur:
                streak += 1
            else :
                ans = max(ans, streak)
                streak = 1
        return max(ans, streak)