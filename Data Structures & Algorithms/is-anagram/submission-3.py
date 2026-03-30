class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*26
        sL = len(s)
        tL = len(t)
        for i in range(max(sL, tL)) :
            if i<sL :
                a[ord(s[i])-ord('a')] -= 1
            if i< tL :
                a[ord(t[i])-ord('a')] += 1
        return a==[0]*26