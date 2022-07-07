from visual import *


class Create_Draw:
    vertices = 0
    Graph = nx.DiGraph()
    start_vertex = 0

    def get_graph(self):
        return self.Graph

    def get_start_vertex(self):
        return self.start_vertex

    def set_vertices(self, vertices_):
        self.vertices = vertices_

    def set_start_vertex(self, start_vertex_):
        self.start_vertex = start_vertex_

    def ReadGraph(self, file_name):
        self.Graph = nx.DiGraph()
        f = open(file_name)
        self.vertices = int(f.readline())
        wtMatrix = []
        for i in range(self.vertices):
            list1 = list(map(int, (f.readline()).split()))
            wtMatrix.append(list1)
        self.start_vertex = int(f.readline())  # исходная вершина, с которой должны начинаться алгоритмы
        for i in range(self.vertices):  # добавляет ребра с весами
            for j in range(len(wtMatrix[i])):
                if wtMatrix[i][j] > 0:
                    self.Graph.add_edge(i, j, length=wtMatrix[i][j])

    def CreateGraph(self, matrix):
        self.Graph = nx.DiGraph()
        wtMatrix = []
        list1 = list(map(int, matrix.split()))
        j = 0
        j1 = self.vertices
        for i in range(self.vertices):
            list2 = list1[j:j1]
            j += self.vertices
            j1 += self.vertices
            wtMatrix.append(list2)
        for i in range(self.vertices):
            for j in range(len(wtMatrix[i])):
                if wtMatrix[i][j] > 0:
                    self.Graph.add_edge(i, j, length=wtMatrix[i][j])

    def DrawGraph(self):
        pos = nx.spring_layout(self.Graph)
        nx.draw(self.Graph, pos, with_labels=True)  # with_labels=true предназначен для отображения номера узла
        edge_labels = dict([((u, v,), d['length']) for u, v, d in self.Graph.edges(data=True)])
        nx.draw_networkx_edge_labels(self.Graph, pos, edge_labels=edge_labels, label_pos=0.3,
                                     font_size=11)  # печатает вес
        return pos
