class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product(i):
            p=1
            while (i>0):
                temp=i%10
                p*=temp
                i//=10
            return p
        number=n
        while True:
            if product(number)%t==0:
                return number
            else:
                number+=1


        