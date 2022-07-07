from Create_Draw import *

class BFS_class:
    Graph = nx.DiGraph()
    start_vertex = 0

    def __init__(self, Graph, start_vertex):
        self.Graph = Graph
        self.start_vertex = start_vertex

    def BFS(self, pos):
        visited = [False] * (len(self.Graph.nodes()))
        queue = []
        queue.append(self.start_vertex)
        visited[self.start_vertex] = True
        while queue:
            curr_node = queue.pop(0)
            for i in self.Graph[curr_node]:  # перебирает все возможные вершины, смежные с curr_node
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    nx.draw_networkx_edges(self.Graph, pos, edgelist=[(curr_node, i)], width=2.5, alpha=0.6,
                                           edge_color='r')  # окрашивает посещённые рёбра
