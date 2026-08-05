from collections import defaultdict, deque
from typing import List
class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)
        suspicious = set()
        queue = deque([k])
        while queue:
            method = queue.popleft()
            if method not in suspicious:
                suspicious.add(method)
                for neighbor in graph[method]:
                    if neighbor not in suspicious:
                        queue.append(neighbor)
        can_remove = True
        for a, b in invocations:
            if b in suspicious and a not in suspicious:
                can_remove = False
                break
        if can_remove:
            remaining_methods = [i for i in range(n) if i not in suspicious]
            return remaining_methods
        else:
            return list(range(n))
