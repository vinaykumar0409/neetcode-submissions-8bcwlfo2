class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in strs :
            a = str(sorted(i))
            if a in hashmap :
                hashmap[a].append(i)
            else :
                hashmap[a] = [i]
        return list(hashmap.values())
