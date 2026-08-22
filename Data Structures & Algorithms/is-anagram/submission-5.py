class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        for i in range(len(s)):
            if s[i] not in s1:
                s1[s[i]] = 0
            else:
                s1[s[i]]+= 1
        for i in range(len(t)):
            if t[i] not in s2:
                s2[t[i]] = 0
            else:
                s2[t[i]]+= 1
        return s1 == s2