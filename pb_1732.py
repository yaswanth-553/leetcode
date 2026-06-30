class Solution(object):
    def largestAltitude(self, gain):
        max_altitude = 0
        altitude = 0
        for value in gain:
            altitude += value
            if max_altitude < altitude:
                max_altitude = altitude
        return max_altitude
sol = Solution()
gain = [-5,1,5,0,-7]
print(sol.largestAltitude(gain))