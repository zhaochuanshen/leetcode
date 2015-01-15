'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
'''

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # this is a BFS code
        if not node:
            return None
        queue = []
        d = {}
        newqueue = []
        newNode = UndirectedGraphNode(node.label)
        d[node] = newNode
        queue.append(node)
        while queue:
            x = queue.pop(0)
            for n in x.neighbors:
                try:
                    d[x].neighbors.append(d[n])
                except KeyError:
                    d[n] = UndirectedGraphNode(n.label)
                    d[x].neighbors.append(d[n])
                    queue.append(n)
        return newNode
    '''
    the following algorithm used DFS
    def cloneGraph(self, node):
        d = {}
        def _cloneGraph(node):
            if not node:
                return None
            newNode = UndirectedGraphNode(node.label)
            d[node] = newNode
            for n in node.neighbors:
                try:
                    newNode.neighbors.append(d[n])
                except KeyError:
                    x = _cloneGraph(n)
                    newNode.neighbors.append(x)
            return newNode
        return _cloneGraph(node)
    '''
