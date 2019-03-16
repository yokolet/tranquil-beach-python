class Bipartite:
    def isBipartite(self, graph: 'List[List[int]]') -> 'bool':
        visited = {}
        for vertex in range(len(graph)):
            if vertex not in visited:
                stack = [vertex]
                visited[vertex] = 0
                while stack:
                    v = stack.pop()
                    for n in graph[v]:
                        if n not in visited:
                            stack.append(n)
                            visited[n] = visited[v] ^ 1
                        elif visited[n] == visited[v]:
                            return False
        return True

    def isBipartite2(self, graph: 'List[List[int]]') -> bool:
        visited = {}
        def dfs(node: int, group: int) -> bool:
            if node not in visited:
                visited[node] = group
                for neighbor in graph[node]:
                    if (neighbor in visited and visited[neighbor] == visited[node]) or\
                        (not dfs(neighbor, group ^ 1)):
                        return False
                return True
            return True
        for i in range(len(graph)):
            if not dfs(i, 0): return False
        return True