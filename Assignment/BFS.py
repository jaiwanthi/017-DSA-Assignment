# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:23:09 2024

@author: Administrator
"""

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(graph[vertex] - visited)
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
        if u in graph and v in graph:
            graph[u].add(v)
        else:
            print(f"Error: One or both vertices '{u}' and '{v}' do not exist in the graph.")
    return graph
if __name__ == "__main__":
    graph = create_graph()
    start_vertex = input("Enter the starting vertex for BFS: ").upper()
    if start_vertex in graph:
        bfs_result = bfs(graph, start_vertex)
        print("BFS traversal result:", bfs_result)
    else:
        print("Error: Starting vertex does not exist in the graph.")
