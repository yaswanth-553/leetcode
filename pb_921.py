class Solution(object):
    def minAddToMakeValid(self, s):
        left = 0
        minAdd = 0
        for ch in s:
            if ch == '(':
                left += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    minAdd += 1
        return minAdd + left
        