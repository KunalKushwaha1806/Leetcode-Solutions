class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        sh=startTime[0:2]
        sm=startTime[3:5]
        ss=startTime[6:8]
        eh=endTime[0:2]
        em=endTime[3:5]
        es=endTime[6:8]
        start= int(sh)*3600+int(sm)*60+int(ss)
        end= int(eh)*3600+int(em)*60+int(es)
        return end-start
        