class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Minute hand angle
        m = (360.0 / 60.0) * minutes
        # Hour hand angle (including minute contribution)
        h = (360.0 / 12.0) * hour + (30.0 / 60.0) * minutes
        if h >= 360:
            h -= 360
        # Difference between angles
        res = abs(m - h)
        # Ensure smallest angle
        if res >= 180:
            res = 360 - res
        return res
