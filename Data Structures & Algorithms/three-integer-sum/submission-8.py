class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        print('1')
        nums = sorted(nums)
        for i in range(len(nums)) :
            pairs = []
            left = 0
            right = len(nums) - 1
            while left < right :
                if left == i or right == i :
                    if nums[i] > 0 :
                        left += 1
                    else :
                        right -= 1
                val = nums[left] + nums[right]
                total = val + nums[i]
                if total == 0 :
                    a = sorted([nums[i], nums[left], nums[right]])
                    if a not in pairs  and i!= left and left!=right and i!= right:
                        pairs.append(a)
                    if nums[i] > 0 :
                        left += 1
                    else :
                        right -= 1
                elif total > 0 :
                    right -= 1
                else :
                    left += 1
            for p in pairs :
                if p not in ans :
                    ans.append(p)
        return ans