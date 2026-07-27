class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        num1 = nums[-1] -1
        num2 = nums[-2] -1
        return num1*num2
        