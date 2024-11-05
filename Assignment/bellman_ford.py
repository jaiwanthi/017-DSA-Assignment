# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:20:52 2024

@author: Administrator
"""

def bellman_ford(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                return distances, "Negative weight cycle detected"
    return distances, "No negative weight cycle"
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}
start_vertex = 'A'
distances, message = bellman_ford(graph, start_vertex)
print("Distances from {}: {}".format(start_vertex, distances))
print(message)
