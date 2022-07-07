from Create_Draw import *

class DFS_class:
    Graph = nx.DiGraph()
    start_vertex = 0

    def __init__(self, Graph, start_vertex):
        self.Graph = Graph
        self.start_vertex = start_vertex

    def DFSUtil(self, v, visited, sl):  # рекурсивный поиск в глубину
        visited[v] = True
        sl.append(v)
        for i in self.Graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited, sl)
        return sl

    def DFS(self):
        visited = [False] * (len(self.Graph))
        sl = []  # список, в котором хранится лес dfs, начинающийся с исходного узла
        dfs_stk = []
        dfs_stk.append(self.DFSUtil(self.start_vertex, visited, sl))
        for i in range(len(self.Graph)):
            if visited[i] == False:
                sl = []
                dfs_stk.append(self.DFSUtil(i, visited, sl))
        return dfs_stk

    def DrawDFSPath(self, dfs_stk):
        pos = nx.spring_layout(self.Graph)
        nx.draw(self.Graph, pos, with_labels=True)  # with_labels=true предназначен для отобра-жения номера узла
        edge_labels = dict([((u, v,), d['length']) for u, v, d in self.Graph.edges(data=True)])
        nx.draw_networkx_edge_labels(self.Graph, pos, edge_labels=edge_labels, label_pos=0.3,
                                     font_size=11)  # печатает вес по всем краям
        for i in dfs_stk:
            # если в dfs-лесу более одного узла, то выводим соответствующие ребра
            if len(i) > 1:
                for j in i[:(len(i) - 1)]:
                    if i[i.index(j) + 1] in self.Graph[j]:
                        nx.draw_networkx_edges(self.Graph, pos, edgelist=[(j, i[i.index(j) + 1])], width=2.5, alpha=0.6, edge_color='r')
                    else:
                        for k in i[1::-1]:
                            if k in self.Graph[j]:
                                nx.draw_networkx_edges(self.Graph, pos, edgelist=[(j, k)], width=2.5, alpha=0.6,edge_color='r')
                                break

