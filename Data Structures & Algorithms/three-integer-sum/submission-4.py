class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        # print(nums)
        l = len(nums)
        for i in range(l) :
            pairs = []
            seen = {}
            for j in range(l):
                if j == i :
                    continue
                target = -(nums[i] + nums[j])
                if target in seen and seen[target] > 0:
                    a = sorted([target, nums[j], nums[i]])
                    pairs.append(a)
                    seen[target] -= 1 
                else:
                    seen[nums[j]] = seen.get(nums[j], 0) + 1
            ans.extend(pairs)
        res = []
        for i in ans :
            if i not in res :
                res.append(i)
        return res
         