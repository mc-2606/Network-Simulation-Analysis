import networkx as nx
import osmnx as om

def load_network(network_file, bidirectional):
    return om.graph_from_xml(network_file, simplify=True, bidirectional=bidirectional)

def to_svg(graph, output_file):
    fig, ax = om.plot_graph(
        graph,
        filepath=output_file,
        save=True,
        show=False,
        node_size=5,
        edge_linewidth=0.8,
    )

    return fig, ax