class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph=[[] for i in range(numCourses)]
        for u,v in prerequisites:
            graph[u].append(v)
        vis=[0]*numCourses
        def dfs(idx):
            if vis[idx]==1:
                return False
            if vis[idx]==2:
                return True 
            vis[idx]=1
            for ngh in graph[idx]:
                if not dfs(ngh):
                    return False 
            vis[idx]=2
            return True 

        for c in range(numCourses):
            if not dfs(c):
                return False 
        return True 