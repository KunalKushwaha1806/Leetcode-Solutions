class Solution:
    def combinationSum(self, candidates: List[int], ts: int) -> List[List[int]]:
        ans=[]
        substr=[]
        n=len(candidates)
        def Solve(i,j):
            if j < 0:
                return
            if j == 0:
                ans.append(substr.copy())
                return
            if i < 0:
                return
            substr.append(candidates[i])
            Solve(i,j-candidates[i])
            substr.pop()
            Solve(i-1,j)
        Solve(n-1,ts)
        return ans 