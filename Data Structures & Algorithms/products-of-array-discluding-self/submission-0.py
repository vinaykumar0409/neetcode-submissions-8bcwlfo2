class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)
        s = [1] * L
        e = [1] * L
        for i in range(1, L) :
            s[i] = nums[i-1] * s[i-1]
        for i in range(L-2, -1, -1) :
            e[i] = nums[i+1] * e[i+1]

        res = [0] * L
        for i in range(L) :
            res[i] = s[i] * e[i]
        
        return res