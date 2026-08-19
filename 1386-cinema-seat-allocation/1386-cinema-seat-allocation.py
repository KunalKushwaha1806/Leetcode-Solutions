class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        ans=n*2
        reservedSeats.sort()
        j=0
        # 2-3 --> l1
        # 4-5 --> l2_left
        # 6-7 --> l2_right
        # 8-9 --> l3
        while j < len(reservedSeats):
            current_row=reservedSeats[j][0]
            l1,l2_left,l2_right,l3=False, False, False, False
            while j<len(reservedSeats) and reservedSeats[j][0]==current_row:
                seat = reservedSeats[j][1]
                if seat==2 or seat==3: l1=True
                elif seat==4 or seat==5: l2_left=True
                elif seat==6 or seat==7: l2_right=True
                elif seat==8 or seat==9: l3=True
                j+=1
            
            if (l1 and l2_right)or(l3 and l2_left)or(l2_left and l2_right):
                ans-=2
            elif l1 or l2_left or l2_right or l3:
                ans-=1

        
        return ans 