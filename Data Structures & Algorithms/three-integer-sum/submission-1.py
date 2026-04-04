class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)) :
            j = 0
            k = len(nums) - 1
            while j < i < k :
                target = nums[j] + nums[k]
                if target == -nums[i] :
                    val = sorted([nums[i], nums[j], nums[k]])
                    print(target, nums[i])
                    if val not in ans :
                        ans.append(val)
                    break
                elif target < nums[i] :
                    j += 1
                else :
                    k -= 1
        return ans