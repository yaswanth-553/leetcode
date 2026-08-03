class Solution(object):
    def isPalindrome(self, s):
        c = ''.join(c for c in s if c.isalnum()).lower()
        return c == c[::-1]
        