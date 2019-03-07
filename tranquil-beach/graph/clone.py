from .undirected_graph_node import UndirectedGraphNode
from .node import Node

class Clone:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        head  = Node(node.val, [])
        nodes = {node: head}
        queue = [node]
        while queue:
            cur = queue.pop(0)
            for n in cur.neighbors:
                if n not in nodes:
                    new_node = Node(n.val,[])
                    nodes[n] = new_node
                    nodes[cur].neighbors.append(new_node)
                    queue.append(n)
                else:
                    nodes[cur].neighbors.append(nodes[n])
        return head

    def cloneGraph2(self, node: 'Node') -> 'Node':
        if not node: return None
        queue = [node]
        nodes = {node.label: UndirectedGraphNode(node.label)}
        while queue:
            cur = queue.pop(0)
            cl_cur = nodes[cur.label]
            for n in cur.neighbors:
                if n.label not in nodes:
                    queue.append(n)
                    cl_n = UndirectedGraphNode(n.label)
                    nodes[n.label] = cl_n
                cl_cur.neighbors.append(nodes[n.label])
        return nodes[node.label]