class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums :
            hashmap[i] = hashmap.get(i, 0) + 1
        a = dict(sorted(((hashmap[x],x) for x in hashmap), reverse=True))
        res = []
        for i in a :
            if k == 0 :
                break
            res.append(a[i])
            k -= 1
        return res