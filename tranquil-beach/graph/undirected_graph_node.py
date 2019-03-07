class UndirectedGraphNode:
    def __init__(self, x):
         self.label = x
         self.neighbors = []

    @staticmethod
    def build(g):
        head_value = g['$id']
        queue = [g]
        nodes = {}
        while queue:
            cur = queue.pop(0)
            if '$id' in cur:
                if cur['$id'] in nodes:
                    n = nodes[cur['$id']]
                    n.label = cur['val']
                else:
                    n = UndirectedGraphNode(cur['val'])
                    nodes[cur['$id']] = n
            for neighbor in cur['neighbors']:
                if '$id' in neighbor:
                    queue.append(neighbor)
                if '$ref' in neighbor:
                    if neighbor['$ref'] in nodes:
                        ref = nodes[neighbor['$ref']]
                    else:
                        ref = UndirectedGraphNode(None)
                        nodes[neighbor['$ref']] = ref
                    if ref not in n.neighbors:
                        n.neighbors.append(ref)
                    if n not in ref.neighbors:
                        ref.neighbors.append(n)
        return nodes[head_value]               
