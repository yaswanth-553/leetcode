class Solution(object):
    def firstUniqChar(self, s):
        chars = {}
        for ch in s:
            chars[ch] = chars.get(ch,0)+1
        for i, ch in enumerate(s):
            if chars[ch] == 1:
                return i
        return -1