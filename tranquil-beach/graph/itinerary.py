from collections import defaultdict

class Itinerary:
    def findItinerary(self, tickets: 'List[List[str]]') -> 'List[str]':
        result = []
        if not tickets: return result

        graph = defaultdict(list)
        for s, d in tickets: graph[s].append(d)
        for key in graph: graph[key] = sorted(graph[key])

        def dfs(city):
            while graph[city]:
                dfs(graph[city].pop(0))
            result.append(city)
        
        dfs("JFK")
        return result[::-1]
