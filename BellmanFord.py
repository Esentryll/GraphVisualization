import networkx as nx

inf = float('inf')

class Bellman_class:
    Graph = nx.DiGraph()
    start_vertex = 0

    def __init__(self, Graph, start_vertex):
        self.Graph = Graph
        self.start_vertex = start_vertex

    def bellmanFord(self, pos):
        vertices = len(self.Graph)  # хранит количество узлов
        dist = []  # dist[i] будет содержать кратчайшее расстояние от начальной вершины до i
        parent = [None] * vertices  # parent[i] будет содержать узел, из которого мы пришли
        for i in range(vertices):
            dist.append(inf)

        parent[self.start_vertex] = -1  # начальная точка не им еет родителя
        dist[self.start_vertex] = 0

        for i in range(vertices - 1):
            for u, v, d in self.Graph.edges(data=True):  # релаксация работает путем сокращения расчетного расстояния между вершинами
                if dist[u] + d['length'] < dist[v]:  # сравнивая это расстояние с другими известными расстояниями
                    dist[v] = d['length'] + dist[u]
                    parent[v] = u

        # окрашиваем путь красным
        for v in range(vertices):
            if parent[v] != -1:
                if (parent[v], v) in self.Graph.edges():
                    nx.draw_networkx_edges(self.Graph, pos, edgelist=[(parent[v], v)], width=2.5, alpha=0.6, edge_color='r')
        return
