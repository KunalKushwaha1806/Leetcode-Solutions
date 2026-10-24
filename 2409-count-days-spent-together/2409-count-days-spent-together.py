class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def date_to_day(date: str):
            month,day=int(date[:2]),int(date[3:])
            return sum(days_in_month[:month - 1])+day
        start_a,end_a=date_to_day(arriveAlice),date_to_day(leaveAlice)
        start_b,end_b=date_to_day(arriveBob),date_to_day(leaveBob)
        overlap=min(end_a,end_b)-max(start_a,start_b)+1
        return max(0,overlap)