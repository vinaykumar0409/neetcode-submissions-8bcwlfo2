class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s :
            hashmap[i] = hashmap.get(i, 0) + 1
        for i in t :
            if i not in hashmap :
                return False
            if hashmap[i] == 1 :
                hashmap.pop(i)
            else :
                hashmap[i] -= 1
        return len(hashmap) == 0