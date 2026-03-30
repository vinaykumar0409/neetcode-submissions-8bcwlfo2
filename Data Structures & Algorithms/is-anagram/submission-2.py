class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*26
        for i in range(len(s)) :
            a[ord(s[i])-ord('a')] -= 1
            a[ord(t[i])-ord('a')] += 1
        return a==[0]*26