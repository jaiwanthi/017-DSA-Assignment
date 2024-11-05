# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:00:57 2024

@author: Administrator
"""

def prim_mst(graph, start):
    if start not in graph:
        raise ValueError(f"Start vertex {start} not in graph")
    mst = []                
    visited = set([start])  
    edges = []              
    for to, weight in graph[start].items():
        edges.append((weight, start, to))

    while edges:
        min_edge = None
        min_weight = float('inf')
        for weight, frm, to in edges:
            if to not in visited and weight < min_weight:
                min_edge = (weight, frm, to)
                min_weight = weight
        if min_edge is None:
            raise ValueError("The graph is not connected, so MST cannot be formed.")
        weight, frm, to = min_edge
        visited.add(to)
        mst.append((frm, to, weight))
        edges = [(w, f, t) for w, f, t in edges if t != to]

           for next_to, next_weight in graph[to].items():
            if next_to not in visited:
                edges.append((next_weight, to, next_to))
    return mst

def create_graph():
    graph = {}
    try:
        num_vertices = int(input("Enter the number of vertices: "))
        num_edges = int(input("Enter the number of edges: "))

        for i in range(num_vertices):
            vertex = input(f"Enter name of vertex {i + 1}: ").upper()
            if vertex in graph:
                raise ValueError(f"Duplicate vertex name: {vertex}")
            graph[vertex] = {}

        for i in range(num_edges):
            u, v, weight = input(f"Enter edge {i + 1} (format: vertex1 vertex2 weight): ").upper().split()
            weight = int(weight)
            if u not in graph or v not in graph:
                raise ValueError(f"Vertices {u} or {v} not found in graph")
            if u == v:
                raise ValueError(f"Self-loops are not allowed: {u} -> {u}")
            graph[u][v] = weight
            graph[v][u] = weight  # Assuming undirected graph
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return graph

def main():
    graph = create_graph()
    if not graph:
        print("Graph creation failed due to input errors.")
        return
    start_vertex = input("Enter the starting vertex: ").upper()
    try:
        mst = prim_mst(graph, start_vertex)
        print("Edges in the MST:")
        for frm, to, weight in mst:
            print(f"{frm} - {to} : {weight}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
if __name__ == "__main__":
    main()
