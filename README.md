# Implementation and analysis of shortest path algorithms using Python

## Description

This repository implements and analyses 3 shortest path algorithms in Python:

- Dijkstra's
- Floyd-Warshall
- Bellman-Ford

*This project was made during my Graph theory course in university.*

## Summary

These algorithms find the shortest path between 2 vertices in a **weighted** graph. A graph is a collection of **vertices** connected by **edges**, which can represent real networks. For **example** in a computer network, the computers are the vertices and the connections between them are the edges (i.e. cables). In a weighted graph, each edge has an associated value attached to it, which represents the cost, the distance or the time it takes to traverse them. A graph be directed or undirected.

These algorithms have many different applications in the real world, including:

- **Network routing:** Determine the most efficient path for data packets in computer networks.
- **Geographic Information Systems (GIS):** Used in mapping and navigation services (Google maps) to find optimal routes and minimize distances.
- **Robotics:** Path planning for autonomous robots to navigate in environments.
- **VLSI Design:** Find optimal routes for connecting various circuit components such as gates and transistors.

### Dijkstra's

- Invented by Edsger W. Dijkstra in 1956.
- Finds the shortest path from a given vertice to any other vertice. Can also find the shortest path between a given start vertice and a destination vertice.
- Used in graphs where the weights are **positive** numbers.
- Time complexity: $O(n^2)$, where $n$ the number of vertices.

### Floyd-Warshall

- Also known as Floyd or Roy-Warshall, published in it's current form by Robert Floyd.
- Finds shortest path between **all** pairs of vertices.
- Can be used in graphs where the weights are either positive or negative.
- Time complexity: $O(n^3)$, where $n$ the number of vertices.

### Bellman-Ford

- Proposed Alfonso Shimbel but got named after Richard Bellman and Lester Ford Jr.
- Finds the shortest path from a given vertice to any other vertice. Can also find the shortest path between a given start vertice and a destination vertice.
- Slower than Dijkstra's, but more flexible since it can be used in graphs with positive or negative weights.
- Time complexity: $O(n*m)$, where $n$ the number of vertices, $m$ the number of edges.

## Example graphs used

A visualization of the graphs used in code.

### Example 1

![Example graph 1](https://github.com/ChrisTs8920/shortest-path-algorithms/blob/main/graphs/ex1.png?raw=true)

### Example 2

![Example graph 2](https://github.com/ChrisTs8920/shortest-path-algorithms/blob/main/graphs/ex2.png?raw=true)
