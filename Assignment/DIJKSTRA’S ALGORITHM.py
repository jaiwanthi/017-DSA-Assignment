# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:17:49 2024

@author: Administrator
"""

def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    previous_nodes = {v: None for v in graph}
    unvisited = list(graph.keys())

    while unvisited:
        current_node = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_node] == float('inf'):
            break
        unvisited.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
    return distances, previous_nodes

def get_shortest_path(previous_nodes, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    return path[::-1]

def main():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))

    for _ in range(num_vertices):
        vertex = input("Enter vertex name: ")
        edges_input = input(f"Enter edges for {vertex} (format: neighbor:weight, ...): ")
        edges = {}

        for edge in edges_input.split(','):
            neighbor, weight = edge.split(':')
            edges[neighbor.strip()] = int(weight.strip())
        graph[vertex] = edges

    start_vertex = input("Enter the starting vertex: ")
    end_vertex = input("Enter the ending vertex: ")
    distances, previous_nodes = dijkstra(graph, start_vertex)
    shortest_path = get_shortest_path(previous_nodes, start_vertex, end_vertex)
    print("Shortest paths from {}: {}".format(start_vertex, distances))
    print("Shortest path from {} to {}: {}".format(start_vertex, end_vertex, shortest_path))

if __name__ == "__main__":
    main()
