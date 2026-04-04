class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        # print(nums)
        l = len(nums) 
        for i in range(l-1) :
            # print(nums[i])
            j = 0 if i != 0 else 1
            k = l - 1 if i != l - 1 else l - 2
            while j < k :
                if i == j or i == k :
                    break
                target = nums[j] + nums[k]
                # print(nums[i], nums[j], nums[k])
                if target == -(nums[i]) :
                    val = sorted([nums[i], nums[j], nums[k]])
                    # print(nums[i], nums[j], nums[k])
                    if val not in ans :
                        ans.append(val)
                    j += 1
                elif target < nums[i] :
                    j += 1
                else :
                    k -= 1
        return ans