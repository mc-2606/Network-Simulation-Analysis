import networkx as nx
import osmnx as ox
from networkx.drawing.nx_pydot import to_pydot

from src.loader import load_network

G = load_network("networks/map1.osm", bidirectional=True)
