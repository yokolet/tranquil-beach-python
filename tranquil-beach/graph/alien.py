from collections import defaultdict

class Alien:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = defaultdict(list)
        nodes = set()
        def build():
            prev = words[0]
            for c in prev:
                nodes.add(c)
            for cur in words[1:]:
                for c in cur:
                    nodes.add(c)
                i, j = 0, 0
                while i < len(prev) and j < len(cur):
                    if prev[i] == cur[j]:
                        i += 1
                        j += 1
                    else:
                        graph[prev[i]].append(cur[j])
                        break
                prev = cur

        def dfs(node):
            visiting.add(node)
            for child in graph[node]:
                if child not in visited:
                    if child in visiting: # cycle
                        return False
                    else:
                        if not dfs(child): return False
            visited.add(node)
            result.append(node)
            return True

        build()
        result = []
        visited = set()
        visiting = set()
        for node in list(nodes):
            if node not in visited:
                if not dfs(node):
                    return ""
        return ''.join(result[::-1])

    def alienOrder4(self, words: 'List[str]') -> str:
        d={}
        chars=set()
        for w in words:
            chars.update(list(w))
        for w1, w2 in zip(words, words[1:]):
            for i, j in zip(w1, w2):
                if i!=j:
                    d.setdefault(i, []).append(j)
                    break
        visited, res=set(),[]
        def dfs(c, path):
            #print(c, visited)
            if c in visited:
                if 0<=path.index(c)<len(path)-1:
                    return True
                return False
            visited.add(c)
            if c in d:
                for i in d[c]:
                    print(i, c, res)
                    if dfs(i, path+i):
                        return True
            res.insert(0, c)
            return False
        for k in chars:
            if dfs(k, k):
                return ""
        return "".join(res)
    
    def alienOrder2(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        N = 26
        adj = [[False] * N for _ in range(N)]
        visited = [-1] * N
        def build():
            prev = words[0]
            for c in prev:
                visited[ord(c) - ord('a')] = 0
            for cur in words[1:]:
                for c in cur:
                    visited[ord(c) - ord('a')] = 0
                i, j = 0, 0
                while i < len(prev) and j < len(cur):
                    if prev[i] == cur[j]:
                        i += 1
                        j += 1
                    else:
                        adj[ord(prev[i]) - ord('a')][ord(cur[j]) - ord('a')] = True
                        break
                prev = cur

        def dfs(i):
            visited[i] = 1
            for j in range(N):
                if adj[i][j]:
                    if visited[j] == 1: return False  # cycle
                    if visited[j] == 0:
                        if dfs(j) == False: return False
            visited[i] = 2
            result.append(chr(i + ord('a')))
            return True

        build()
        result = []
        for i in range(N):
            if visited[i] == 0:
                if dfs(i) == False: return ""

        return ''.join(result[::-1])

    def alienOrder3(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        pre = defaultdict(set)
        suc = defaultdict(set)

        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break
        chars = set(''.join(words))
        charToProcess = chars - set(pre)
        order = ''
        while charToProcess:
            ch = charToProcess.pop()
            order += ch
            for b in suc[ch]:
                pre[b].discard(ch)
                if not pre[b]:
                    charToProcess.add(b)
        return order if set(order) == chars else ''
