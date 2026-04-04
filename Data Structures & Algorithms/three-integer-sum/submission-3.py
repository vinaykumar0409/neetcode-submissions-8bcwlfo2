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
                complement = -(nums[i] + nums[j])
                # If the complement exists and its count is positive, we found a pair
                if complement in seen and seen[complement] > 0:
                    a = sorted([complement, nums[j], nums[i]])
                    pairs.append(a)
                    seen[complement] -= 1  # Decrement count to avoid duplicate pairs
                else:
                    seen[nums[j]] = seen.get(nums[j], 0) + 1
            ans.extend(pairs)
        res = []
        for i in ans :
            if i not in res :
                res.append(i)
        return res
         
        # for i in range(l) :
        #     # print(nums[i])
        #     j = 0 if i != 0 else 1
        #     k = l - 1 if i != l - 1 else l - 2
        #     hashmap = {}
        #     tempAns = []
        #     while j < l :
        #         val =  nums[j] + nums[i]
        #         val = -val
        #         if val in hashmap :
        #             indexes = sorted([nums[j], nums[hashmap[val]], nums[i]])
        #             if indexes not in tempAns and sum(indexes) == 0:
        #                 print(sum(indexes), indexes)
        #                 tempAns.append(indexes)
        #         else :
        #             hashmap[nums[j]] = j
        #         j += 1
        #     ans.extend(tempAns)
        # return set(ans)