class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_arr = sorted(set(arr))
        rank = {}
        for i, val in enumerate(sorted_arr):
            rank[val] = i+1
        return [rank[x] for x in arr]