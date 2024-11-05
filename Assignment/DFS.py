# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:23:44 2024

@author: Administrator
"""

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph[start] - visited:
        result.extend(dfs(graph, neighbor, visited))
    return result
def create_graph():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))
    for i in range(num_vertices):
        vertex = input(f"Enter name of vertex {i + 1}: ").upper()
        graph[vertex] = set()
    for i in range(num_edges):
        u, v = input(f"Enter edge {i + 1} (format: vertex1 vertex2): ").upper().split()
        graph[u].add(v)
if __name__ == "__main__":
    graph = create_graph()
    start_vertex = input("Enter the starting vertex for DFS: ").upper()
    if start_vertex in graph:
        dfs_result = dfs(graph, start_vertex)
        print("DFS traversal result:", dfs_result)
    else:
        print("Error: Starting vertex does not exist in the graph.")
