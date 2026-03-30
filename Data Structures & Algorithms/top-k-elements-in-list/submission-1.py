class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums :
            hashmap[i] = hashmap.get(i, 0) + 1
        
        ans = []
        hashmap = dict(sorted(hashmap.items(), key = lambda item:item[1], reverse=True))
        for i in hashmap:
            if k == 0 :
                return ans
            ans.append(i)
            k -= 1
        return ans