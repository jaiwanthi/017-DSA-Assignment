# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:21:23 2024

@author: Administrator
"""

def floyd_warshall(graph):
    dist = {u: {v: float('inf') for v in graph} for u in graph}
    for u in graph:
        dist[u][u] = 0
        for v, weight in graph[u].items():
            dist[u][v] = weight
    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
graph = {
    'A': {'B': 3, 'C': 8},
    'B': {'C': 2, 'D': 1},
    'C': {'D': 4},
    'D': {'A': 7}
}
distances = floyd_warshall(graph)
for u in distances:
    for v in distances[u]:
        print(f"The shortest distance from {u} to {v} is {distances[u][v]}")

