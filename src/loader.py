"""
For actual implementation of methods, I will stick to using the networkx and osmn library. However,
I have also buuilt my own graph properties from the first principle definitions
"""

import networkx as nx
import osmnx as om

def load_network(network_file, bidirectional):
    # Using basic homeomorphic graph structures, will first discovere properties of undirected graphs
    return om.graph_from_xml(network_file, simplify=True, bidirectional=bidirectional)

def to_svg(graph, output_file):
    # Plot grpah, check valid network and osm file
    fig, ax = om.plot_graph(
        graph,
        filepath=output_file,
        save=True,
        show=False,
        node_size=5,
        edge_linewidth=0.8,
    )

    return fig, ax