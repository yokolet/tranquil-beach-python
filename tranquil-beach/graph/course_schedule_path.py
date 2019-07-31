class CourseSchedulePath:
    def findOrder(self, numCourses: int, prerequisites: 'List[List[int]]') -> 'List[int]':
        graph = {i: [] for i in range(numCourses)}
        for req in prerequisites:
            graph[req[0]].append(req[1])

        def topSort(node):
            if visited[node] != 0: return visited[node]
            visited[node] = 1 # visiting
            for c in graph[node]:
                if topSort(c) == 1:
                    return 1
            result.append(node)
            visited[node] = 2 # visited
            return 0

        result = []
        visited = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if visited[i] == 0:
                if topSort(i) == 1:
                    return []
        return result