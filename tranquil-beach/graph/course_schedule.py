class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: 'List[List[int]]') -> bool:
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            graph[pre].append(cur)
            in_degree[cur] += 1
        finished = [i for i in range(numCourses) if in_degree[i] == 0]
        if len(finished) == 0: return False
        for i in finished:
            for c in graph[i]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    finished.append(c)
        return numCourses == len(finished)
