#hashmap where key is letter and value is num of times it appears

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charcount1 = {}
        charcount2 = {}
        for letter in s:
            if letter in charcount1:
                charcount1[letter] += 1
            else:
                charcount1[letter] = 1
        for letter in t:
            if letter in charcount2:
                charcount2[letter] += 1
            else:
                charcount2[letter] = 1
        if charcount1 == charcount2:
            return True
        else:
            return False