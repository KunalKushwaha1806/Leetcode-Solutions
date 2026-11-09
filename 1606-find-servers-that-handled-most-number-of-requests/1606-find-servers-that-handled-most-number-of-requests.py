class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy = [] 
        free = list(range(k)) 
        freq = [0]*k
        for i, (ta, tl) in enumerate(zip(arrival, load)): 
            while busy and busy[0][0] <= ta: 
                _, ii = heappop(busy)
                heappush(free, i + (ii - i) % k)
            if free: 
                ii = heappop(free) % k 
                freq[ii] += 1
                heappush(busy, (ta+tl, ii))
        mx = max(freq)
        return [i for i, x in enumerate(freq) if x == mx]