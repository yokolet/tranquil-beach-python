from collections import defaultdict

class MinRectangle:
    def minAreaRect(self, points: 'List[List[int]]') -> int:
        n = len(points)
        x2y, y2x = defaultdict(set), defaultdict(set)
        for x, y in points:
            x2y[x].add(y)
            y2x[y].add(x)
        if len(x2y) == n or len(y2x) == n: return 0
        min_area = float('inf')
        for x, ys in x2y.items():
            ys = list(ys)
            for i in range(len(ys)-1):
                for j in range(i+1, len(ys)):
                    y1, y2 = ys[i], ys[j]
                    for x2 in (y2x[y1] & y2x[y2] - {x}):
                        area = abs(x-x2) * abs(y1-y2)
                        min_area = min(min_area, area)
        return 0 if min_area == float('inf') else min_area


    def minAreaRect2(self, points: 'List[List[int]]') -> int:
        x2y = defaultdict(set)
        for x, y in points:
            x2y[x].add(y)
        min_area = float('inf')
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                if points[i][0] == points[j][0] or\
                    points[i][1] == points[j][1]:
                    continue;
                if points[j][1] in x2y[points[i][0]] and\
                    points[i][1] in x2y[points[j][0]]:
                    area = abs(points[i][0] - points[j][0]) *\
                        abs(points[i][1] - points[j][1])
                    min_area = min(min_area, area)
        return 0 if min_area == float('inf') else min_area