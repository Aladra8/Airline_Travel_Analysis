# graph_algorithms.py
import networkx as nx

import networkx as nx

def create_graph(meta_data, reachability_data):
    G = nx.DiGraph()

    # Add nodes
    for _, row in meta_data.iterrows():
        G.add_node(row['node_id'], name=row['name'], population=row['population'])

    # Add edges with weights
    for edge_data in reachability_data:
        G.add_edge(edge_data['source'], edge_data['target'], weight=edge_data['travel_time'])

    return G

def calculate_network_metrics(graph):
    # Calculate various network metrics
    degree_centrality = nx.degree_centrality(graph)
    betweenness_centrality = nx.betweenness_centrality(graph)
    pagerank = nx.pagerank(graph)
    clustering_coefficient = nx.average_clustering(graph)

    return degree_centrality, betweenness_centrality, pagerank, clustering_coefficient
