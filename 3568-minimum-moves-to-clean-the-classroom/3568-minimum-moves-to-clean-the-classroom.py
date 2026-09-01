from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        litter_map = {}
        start = None
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_map[(r, c)] = len(litter_map)
                    
        total_litter = len(litter_map)
        target_mask = (1 << total_litter) - 1
        
        if total_litter == 0:
            return 0
        
        best_energy = {}
        
        sr, sc = start
        queue = deque([(sr, sc, 0, energy, 0)])
        best_energy[(sr, sc, 0)] = energy
        
        while queue:
            r, c, mask, e, steps = queue.popleft()
            
            if mask == target_mask:
                return steps
            
            if e <= 0:
                continue
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_e = energy if classroom[nr][nc] == 'R' else e - 1
                    
                    next_mask = mask
                    if (nr, nc) in litter_map:
                        next_mask |= (1 << litter_map[(nr, nc)])
                    
                    state = (nr, nc, next_mask)
                    
                    if next_e > best_energy.get(state, -1):
                        best_energy[state] = next_e
                        queue.append((nr, nc, next_mask, next_e, steps + 1))
                        
        return -1