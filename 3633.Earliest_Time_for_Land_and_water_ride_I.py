class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        min_time = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land_done = landStartTime[i] + landDuration[i]
                water_do = max(waterStartTime[j], land_done)
                finish1 = water_do + waterDuration[j]
                water_done = waterStartTime[j] + waterDuration[j]
                land_do = max(landStartTime[i], water_done)
                finish2 = land_do + landDuration[i]
                min_time = min(min_time, finish1, finish2)
        return min_time
