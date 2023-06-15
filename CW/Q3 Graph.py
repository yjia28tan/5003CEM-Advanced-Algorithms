class WeightedGraph:
    # Constructor
    def __init__(self, edges, n):
        # # allocate memory for the adjacency list
        # self.adjacencyList = [[] for _ in range(n)]
        #
        # # add edges to the directed graph
        # for (src, destination, weight) in edges:
        #     # allocate node in adjacency list from src to destination with weight
        #     self.adjacencyList[src].append((destination, weight))
        self.adjList = {}

        for (src, dest, weight) in edges:
            if src not in self.adjList:
                self.adjList[src] = []
            self.adjList[src].append((dest, weight))

    # Function to list all adjacent Vertices
    def listAdjacentVertex(self, vertex):
        # return [adj_vertex for (adj_vertex, _) in self.adjacencyList[vertex]]
        return [adj_vertex for (adj_vertex, _) in self.adjList[vertex]]
        # iterates over the tuples in the sublist of the adjacency list for a specific vertex,
        # extracts the adjacent vertices, and returns them as a list.

    # Function to calculate the sum of all the weight for all the adjacent Vertices of a graph
    def sumHighestAdjacentVertex(self, vertex):
        adj_list = self.listAdjacentVertex(vertex)
        if not adj_list:
            return 0  # If there are no adjacent vertices, it means the given vertex has no outgoing edges.
            # the function returns 0 as there are no weights to sum.
        return sum([weight for (_, weight) in self.adjList[vertex]])


# Function to print adjacency list representation of a graph
# def printWeightedGraph(graph):
#     for src in range(len(graph.adjacencyList)):
#         # print current vertex and all its neighboring vertices with weights
#         for (destination, weight) in graph.adjacencyList[src]:
#             print(f'({src} —({weight})—> {destination}) ', end='')
#         print()
def printWeightedGraph(graph):
    for src in graph.adjList:
        # print current vertex and all its neighboring vertices with weights
        for (destination, weight) in graph.adjList[src]:
            print(f'({src} —({weight})—> {destination}) ', end='')
        print()

if __name__ == '__main__':
    # Edges and weights in a directed weighted graph
    edges1 = [('A', 1, 31), ('A', 6, 13),
              (1, 2, 11), (1, 3, 9), (1, 8, 10),
              (2, 'A', 8),
              (3, 8, 5), (3, 5, 14),
              (8, 3, 12),
              (5, 2, 7), (5, 3, 3)]
    edges2 = [('A', 1, 2), ('A', 2, 4), ('A', 6, 6),
              (1, 6, 8), (1, 4, 4),
              (2, 'A', 6), (2, 4, 2),
              (6, 4, 5),
              (4, 5, 10)]

    # No. of vertices
    n = 6

    # construct a graph from a given list of edges
    graph1 = WeightedGraph(edges1, n)
    graph2 = WeightedGraph(edges2, n)

    # print adjacency list representation of the graph
    print("Graph 1")
    printWeightedGraph(graph1)
    for vertex in graph1.adjList:
        print("\nAdjacent vertices of vertex", vertex, ":", graph1.listAdjacentVertex(vertex))
        print("Sum of the weights of adjacent vertices of vertex", vertex, ":", graph1.sumHighestAdjacentVertex(vertex))

    print("\n\nGraph 2")
    printWeightedGraph(graph2)
    for vertex in graph2.adjList:
        print("\nAdjacent vertices of vertex", vertex, ":", graph2.listAdjacentVertex(vertex))
        print("Sum of the weights of adjacent vertices of vertex", vertex, ":", graph2.sumHighestAdjacentVertex(vertex))


"""References:
‘Graph Data Structure’ (n.d.) in BogoToBogo 
https://www.bogotobogo.com/python/python_graph_data_structures.php

Graph Implementation in Python (n.d.) 
https://www.techiedelight.com/graph-implementation-python/
"""
