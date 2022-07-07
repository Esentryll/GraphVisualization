import networkx as nx
import sys

class Dijsktra_class:
    Graph = nx.DiGraph()
    start_vertex = 0

    def __init__(self, graph, start_vertex):
        self.Graph = graph
        self.start_vertex = start_vertex

    def min_dist(self, dist, sptSet, vertices):
        min = sys.maxsize
        min_index = 0
        for v in range(vertices):
            if sptSet[v] == False and dist[v] <= min:
                min = dist[v]
                min_index = v
        return min_index

    def dijsktras(self, pos):
        vertices = len(self.Graph)  # хранит количество вершин
        dist = []  # dist[i] будет содержать кратчайшее расстояние от начальной вершины до i
        parent = [None] * vertices  # parent[i] будет содержать узел, из которого мы пришли
        sptSet = []  # sptSet[i] будет true, если вершина i включена в кратчайший путь
        # изначально для каждого узла dist[] имеет максимальное значение, а sptSet[] имеет значение False
        for i in range(vertices):
            dist.append(sys.maxsize)
            sptSet.append(False)

        parent[self.start_vertex] = -1  # начальная вершина не имеет родителя
        dist[self.start_vertex] = 0
        for count in range(vertices - 1):
            u = self.min_dist(dist, sptSet, vertices)  # выбираем ближайшую по расстоянию вершину
            sptSet[u] = True
            # смотрим смежные вершины
            for v in range(vertices):
                if (u, v) in self.Graph.edges():
                    if sptSet[v] == False and dist[u] != sys.maxsize and dist[u] + self.Graph[u][v]['length'] < dist[v]:
                        dist[v] = dist[u] + self.Graph[u][v]['length']
                        parent[v] = u
        # окрашиваем путь красным
        for X in range(vertices):
            if parent[X] != -1:
                print(parent[X])
                if (parent[X], X) in self.Graph.edges():
                    nx.draw_networkx_edges(self.Graph, pos, edgelist=[(parent[X], X)], width=2.5, alpha=0.6, edge_color='r')

