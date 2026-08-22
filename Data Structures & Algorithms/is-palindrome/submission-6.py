class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        length = len(cleaned)
        for i in range(length):
            backIndex = length - 1 - i
            if (cleaned[i] == " "):
                i += 1
            if (cleaned[backIndex] == " "):
                backIndex += 1
            if (cleaned[i] != cleaned[backIndex]):
                return False
        return True