class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return
        pos={}
        for i in range(len(nums)):
            if nums[i] not in pos:
                pos[nums[i]]=[i]
            else:
                pos[nums[i]].append(i)
        unique_n=sorted(pos.keys())
        take = 0
        skip = 0

        for i in range(len(unique_n)):
            val=unique_n[i]
            points=val*len(pos[val])
            if i>0 and unique_n[i - 1]==val - 1:
                new_take=skip+points
            else:
                new_take=max(take,skip)+points
            new_skip=max(take,skip)
            take,skip=new_take,new_skip

        return max(take,skip)
