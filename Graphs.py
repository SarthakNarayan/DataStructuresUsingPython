from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSPrinter(self,v,visited):
        visited[v-1] = True
        print(v , end=" ")
        for i in self.graph[v]:
            if visited[i-1] == False:
                self.DFSPrinter(i,visited)

    def DFS_Disconnected(self):
        visited = [False]*len(self.graph)
        for i in range(len(self.graph)): 
            if visited[i-1] == False: 
                self.DFSPrinter(i, visited)

    def DFS(self,v):
        visited = [False]*len(self.graph)
        self.DFSPrinter(v, visited)

    def BFS(self,s):
        queue = []
        visited = [False]*(len(self.graph))
        queue.append(s)
        visited[s-1] = True
        while queue:
            s = queue.pop(0)
            print(s , end=" ")
            for i in self.graph[s]:
                if visited[i-1] == False:
                    queue.append(i)
                    visited[i-1] = True

g = Graph() 
g.addEdge(1, 2) 
g.addEdge(1, 3) 
g.addEdge(2, 1) 
g.addEdge(3, 1) 
g.addEdge(2, 4) 
g.addEdge(2, 5) 
g.addEdge(3, 5) 
g.addEdge(4, 2) 
g.addEdge(5, 2) 
g.addEdge(5, 3) 
g.addEdge(4, 6) 
g.addEdge(5, 6) 
g.addEdge(6, 4) 
g.addEdge(6, 5) 
g.addEdge(5, 4)
  
print("Graph Looks like")
print(g.graph)
print("BFS")
g.BFS(1)
print("\nDFS")
g.DFS(1)