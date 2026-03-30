class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums :
            hashmap[i] = hashmap.get(i, 0) + 1
        a = dict(sorted(hashmap.items(), key= lambda item: item[1], reverse=True))
        res = []
        for i in a :
            if k == 0 :
                break
            res.append(i)
            k -= 1
        return res