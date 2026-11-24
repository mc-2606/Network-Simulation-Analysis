import networkx as nx
import osmnx as ox

"""
Despite networkx and osmnx having their own built in graph properties, I am also implmeneting my own graph properties to be used in the simulation. This is because I want to have a more flexible and customizable way of defining and calculating graph properties defined in some of my modules
"""

class NetworkProperties:
    def __init__(self, graph: nx.MultiDiGraph, directed: bool = False):
        self.graph = graph
        self.directed = directed

    def calculate_average_degree_by_edges(self):
        """
        Calculates the average degree of the graph using eulers handshaking lemma
        Average degree is defined as the sum of edges divided by 2
        Assumes graph is undirected
        """
        total_edges = self.graph.number_of_edges()

        return total_edges / 2

    def calculate_average_degree_by_nodes(self):
        """
        Average degree is defined as the sum of edges divided by number of nodes
        Assumes graph is undirected
        """
        total_edges = self.graph.number_of_edges()
        total_nodes = self.graph.number_of_nodes()

        return total_edges / total_nodes
