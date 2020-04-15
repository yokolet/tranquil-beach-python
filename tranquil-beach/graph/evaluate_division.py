from collections import deque

class EvaluateDivision:
    def calcEquation(self, equations: 'List[List[str]]',
                            values: 'List[float]',
                            queries: 'List[List[str]]') -> 'List[float]':
        def buildGraph():
            g = {}
            for i in range(len(equations)):
                s, d, v = equations[i][0], equations[i][1], values[i]
                if s not in g:
                    g[s] = [(s, 1)]
                if d not in g:
                    g[d] = [(d, 1)]
                g[s].append((d, v))
                g[d].append((s, 1/v))
            return g

        def search(s, d):
            if s not in graph or d not in graph:
                return -1.0
            queue = deque([(s, 1)])
            seen = {s}
            while queue:
                cur_n, cur_v = queue.popleft()
                for next_n, next_v in graph[cur_n]:
                    if next_n == d: return cur_v * next_v
                    elif next_n not in seen:
                        seen.add(next_n)
                        queue.append((next_n, cur_v * next_v))
            return -1.0

        graph = buildGraph()
        return [search(s, d) for s, d in queries]
