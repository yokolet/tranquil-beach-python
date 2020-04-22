from collections import defaultdict
import heapq

class NetworkDelay:
    def networkDelayTime(self, times: 'List[List[int]]', N: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        path = {}
        queue = [(0, K)]
        while queue:
            cur_w, cur_n = heapq.heappop(queue)
            if cur_n in path: continue
            path[cur_n] = cur_w
            for next_n, next_w in graph[cur_n]:
                if next_n not in path:
                    heapq.heappush(queue, (cur_w + next_w, next_n))
        return max(path.values()) if len(path) == N else -1
