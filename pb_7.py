class Solution(object):
    def reverse(self, x):
        ans = int(str(x)[::-1]) if x >= 0 else -int(str(x)[:0:-1])
        if -2**31 <= ans <= 2**31:
            return ans
        return 0
sol = Solution()
x = -321
print(sol.reverse(x))