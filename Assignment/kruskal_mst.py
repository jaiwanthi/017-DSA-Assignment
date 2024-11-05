# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:01:18 2024

@author: Administrator
"""

class Edge:
    def __init__(self, u, v, weight):
        self.u = u  
        self.v = v  
        self.weight = weight
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices          
        self.edges = []                 
    def add_edge(self, u, v, weight):
                self.edges.append(Edge(u, v, weight))
    def find_parent(self, parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return self.find_parent(parent, parent[vertex])

    def union(self, parent, rank, u, v):
        # Union operation by rank
        root_u = self.find_parent(parent, u)
        root_v = self.find_parent(parent, v)
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

    def kruskal_mst(self):
        for i in range(len(self.edges)):
            for j in range(i + 1, len(self.edges)):
                if self.edges[i].weight > self.edges[j].weight:
                    self.edges[i], self.edges[j] = self.edges[j], self.edges[i]

        mst = []                 
        parent = {}              
        rank = {}                
        for vertex in range(self.vertices):
            parent[vertex] = vertex
            rank[vertex] = 0
        for edge in self.edges:
            u = edge.u
            v = edge.v
            root_u = self.find_parent(parent, u)
            root_v = self.find_parent(parent, v)
            if root_u != root_v:
                mst.append(edge)
                self.union(parent, rank, root_u, root_v)
        return mst
def create_graph():
    try:
        num_vertices = int(input("Enter the number of vertices: "))
        num_edges = int(input("Enter the number of edges: "))
        graph = Graph(num_vertices)
        for i in range(num_edges):
            u, v, weight = map(int, input(f"Enter edge {i + 1} (format: vertex1 vertex2 weight): ").split())
            if u < 0 or v < 0 or u >= num_vertices or v >= num_vertices:
                raise ValueError(f"Invalid vertices: {u} or {v} out of range.")
            if u == v:
                raise ValueError("Self-loops are not allowed.")
            graph.add_edge(u, v, weight)
        return graph

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    graph = create_graph()
    if not graph:
        print("Graph creation failed due to input errors.")
        return
    try:
        mst = graph.kruskal_mst()
        print("Edges in the MST:")
        for edge in mst:
            print(f"{edge.u} - {edge.v} : {edge.weight}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
